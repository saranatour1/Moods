from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from pytz import all_timezones     #importing all time zones in the pyz library
from .models import *
# Create your views here.
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
                return redirect('/dashboard')
            else:
                messages.error(request, 'Invalid password')
        else:
            messages.error(request, 'Invalid email')
    return redirect('/')

def dashboard(request):
  return HttpResponse("You have logged in successfully")


def logout(request):
  request.session.flush()
  return redirect('/')