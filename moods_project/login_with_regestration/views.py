from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from pytz import all_timezones   #importing all time zones in the pyz library
from .models import *
# Create your views here.
import pytz
import bcrypt

# referring to the main login method
def show_login_page(request):
  return render(request, "login.html ")


# referring to the main regestration page 
def show_registration_page(request):
  time_zones = all_timezones
  context = {'time_zones': time_zones}
  return render(request,"register.html",context)

#create a new user object where the values are handles as form data
def handle_regestration(request):
    if request.method=='POST':
        errors=User.objects.validate_login(request.POST)
        if len(errors) > 0:
            error_list = []
            for key, value in errors.items():
                error_list.append(value)
            return JsonResponse({'success': False, 'errors': error_list}) #removed the redirection 
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email=request.POST['email'],
                                birthday=request.POST['birthday'],
                                gender=request.POST['gender'],
                                time_zone=request.POST['time_zone'],
                                password_hash=pw_hash)
            newUser=User.objects.last().id
            request.session['newUser'] = newUser
            # return redirect('/dashboard')
            return JsonResponse({'success': True}) #returned true instead of redirection 
    else:
        return redirect('/')


# Making the logged user log in to the wall app not to the success page
def successfull(request):
    if 'newUser' in request.session:
        return redirect('/dashboard')
    else:
        return redirect('/')

# route to handle login 

def handle_login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email']).first()
        if user:
            if bcrypt.checkpw(request.POST['password'].encode(), user.password_hash.encode()):
                request.session['newUser'] = user.id
                return JsonResponse({'success': True})
            else:
                  return JsonResponse({'success': False, 'errors': ['Invalid email or password']})
        else:
              return JsonResponse({'success': False, 'errors': ['Invalid email or password']})
    return JsonResponse({'success': False, 'errors': ['please try again']})



# The main dashboard page at route  /dashboard 
def dashboard(request):
  # user profile front view done
  user_id=request.session['newUser']
  newUser=User.objects.get(id=user_id)
  user_age= datetime.date.today()- newUser.birthday 
  age= (user_age.days//365)
  time_zone=newUser.time_zone
  current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
  current_time_str = current_time.strftime('%H:%M:%S')
  current_date_str = current_time.strftime('%Y-%m-%d')
  
  context= {
    'newUser':newUser,
    'user_age':age,
    'current_time':current_time_str,
    'current_date':current_date_str, 
  }
  return render(request,"dashboard.html",context)


def logout(request):
  request.session.flush()
  return redirect('/')

# the profile pag of the loged user

def logged_user_profile(request):
  if 'newUser' in request.session:
    user_id=request.session['newUser']
    newUser=User.objects.get(id=user_id)
    user_age= datetime.date.today()- newUser.birthday 
    age= (user_age.days//365)
    time_zone=newUser.time_zone
    current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
    current_time_str = current_time.strftime('%H:%M:%S')
    current_date_str = current_time.strftime('%Y-%m-%d')
    
    context={
    'newUser':newUser,
    'user_age':age,
    'current_time':current_time_str,
    'current_date':current_date_str, 
    }
    return render(request, "userprofile.html", context)
