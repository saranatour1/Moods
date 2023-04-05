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
            request.session['id'] = newUser 
            # هاي انا ضفتها ببببببببببببببببببببببببببب
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
                request.session['id'] = user.id 
                # هاي انا ضفتها ببببببببببببببببببببببببببب
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

# other users profile 
def other_user_profile(request,user_id):
  logged_user_id=request.session['newUser']
  newUser=User.objects.get(id=logged_user_id)
  user=User.objects.get(id=user_id)
  user_age= datetime.date.today()- user.birthday 
  age= (user_age.days//365)
  time_zone=user.time_zone
  current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
  current_time_str = current_time.strftime('%H:%M:%S')
  current_date_str = current_time.strftime('%Y-%m-%d')
  context={
    
    "user":user,
    'user_age':age,
    'current_time':current_time_str,
    'current_date':current_date_str, 
  }
  return render(request, "otheruserprofile.html",context)


# -----------------------hamza start


# -------------------------friendshipStart
def requestAdd(request,frindId):
    sender = User.objects.get(id = request.session['id'])
    reciever = User.objects.get(id = int(frindId))
    Request.objects.create(request_sender = sender,request_reciever = reciever )
    return redirect('/otherProf/' + str(frindId))


def requestDelete(request,frindId):
    user = User.objects.get(id = request.session['id'])
    other = User.objects.get(id = int(frindId))
    user.sent_requests.delete(other)
    user.received_requests.delete(other)
    return redirect('/userProf') 

def frindAdd(request,frindId):
    user = User.objects.get(id = request.session['id'])
    friend = User.objects.get(id = int(frindId))
    user.friends.add(friend)
    user.received_requests.delete(friend)
    return redirect('/userProf')

def frindRemove(request,frindId):
    user = User.objects.get(id = request.session['id'])
    friend = User.objects.get(id = int(frindId))
    user.friends.remove(friend)
    return redirect('/otherProf/' + str(frindId)) 

# -------------------------friendshipEnd



def likeOnPost(request,postId):
    user = User.objects.get(id = request.session['id'])
    post = Post.objects.get(id = postId)
    LikePost.objects.create(user_who_like = user,post = post)
    post.likeCount += 1
    post.save()
    return redirect('/dashboard')


# -------------------------startmessage
def messages(request):
    
    if 'otherId' not in request.session :
        if User.objects.last().id:
            otherId = User.objects.last().id
            request.session['otherId'] = otherId
            return redirect('/messages')
        else:
            all_users = User.objects.all()
            context ={
                'all_users' : all_users,
            }
            return render(request,'messages1.html',context)
    else:
        # ---------------------------saratimestart
        user_id=request.session['otherId']
        newUser=User.objects.get(id=user_id)
        user_age= datetime.date.today()- newUser.birthday 
        age= (user_age.days//365)
        time_zone=newUser.time_zone
        current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
        current_time_str = current_time.strftime('%H:%M:%S')
        current_date_str = current_time.strftime('%Y-%m-%d')
        
        # ------------------------------saratimeend

        request.session['id']=request.session['newUser']
        # all_users_for_last_messages = User.objects.get(id = request.session['id']).chat_groups2.all()
        all_users = User.objects.all() 
        # --------------------------
        user = User.objects.get(id = request.session['id'])
        other = User.objects.get(id=request.session['otherId'])

        # all_users_for_last_messages = OurMessage.objects.filter(user_group1 = user)

        sent = Message.objects.filter(message_receiver = other,message_sender = user)
        
        received = Message.objects.filter(message_sender = other,message_receiver = user)
        
        allSR = received.union(sent)  # messagess

        # ---------------------------------
        userId = request.session['id']
        messages = Message.objects.all().order_by('-created_at')
        arrI = []
        arrP = []
        all_users_for_last_messages = []
        for message in messages:
            if message.message_sender_id == userId and userId not in arrI:
                arrI.append(message.message_receiver_id)
                arrP.append(1)
            elif message.message_receiver_id == userId and userId not in arrI:
                arrI.append(message.message_sender_id)
                arrP.append(0)
        for i in range(len(arrI)):
            if  User.objects.get(id = arrI[i]) not in all_users_for_last_messages:
                all_users_for_last_messages.append(User.objects.get(id = arrI[i]))
        # ---------------------------------S
        context = {
                'allSR': allSR,
                'all_users_for_last_messages': all_users_for_last_messages,
                'all_users' : all_users,
                'sent': sent,
                'received' : received,
                'other':other,
                'theUser' : User.objects.get(id = request.session['id']),
                # هذه الطويلة لعرض قائمة المستخدمين عل يسار


                'newUser':newUser,
                'user_age':age,
                'current_time':current_time_str,
                'current_date':current_date_str, 
                }
        return render(request,'messages.html',context)

def changOtherId(request,otherId):# this func put it in link on the left list in 'messages page'
                                # we use this link to chang the 'other' id
    request.session['otherId'] = otherId
    return redirect('/messages')

def creatMessages(request,otherId):
    message_content = request.POST['message_content']
    message_sender = User.objects.get(id = request.session['id'])
    message_receiver = User.objects.get(id = int(otherId))
    Message.objects.create(message_content = message_content,message_sender = message_sender,message_receiver = message_receiver)
    # message_sender.chat_groups.add(message_receiver)
    OurMessage.objects.create(user_group1 = message_sender, user_group2 = message_receiver)
    
    return redirect('/messages')
# ----------------------------------endmessage



def userProf(request):
    context = {
        'user' : User.objects.get(id = request.session['id'])
    }
    return render(request,'userProf.html',context)


def otherProf(request,otherId):
    request.session['otherId'] = otherId
    context = {
        'other' : User.objects.get(id = request.session['otherId']),
        'user' : User.objects.get(id = request.session['id']),
    }
    return render(request,'otherProf.html',context)


def search(request,se):
    re1 = User.objects.filter(first_name = se)
    re2 = User.objects.filter(last_name = se)
    re3 = User.objects.filter(email = se)
    if re1 or re2 or re3:
        te = 1
    else:
        te = 0
    context = {
        're1':re1,
        're2':re2,
        're3':re3,
        'te':te,
    }
    return render(request,'result.html',context)

def editProfile(request):
    context = {
        'user':User.objects.get(id = request.session['newUser'])
    }
    return render(request,'editProfile.html',context)


def updateProfile(request):

    if request.method=='POST':
        errors=User.objects.validate_login(request.POST)
        if len(errors) > 0:
            error_list = []
            for key, value in errors.items():
                error_list.append(value)
            return JsonResponse({'success': False, 'errors': error_list}) #removed the redirection 
        else:
            first_name =request.POST['first_name']
            last_name =request.POST['last_name']
            birthday =request.POST['birthday']
            gender =request.POST['gender']
            password =request.POST['password']
            user = User.objects.get(id = request.session['newUser'])
            user.first_name = first_name
            user.last_name = last_name
            user.birthday = birthday
            user.gender = gender
            user.password = password
            user.save()
        return JsonResponse({'success': True})
    # return redirect('/edit_profile')

# --------------------------hamza end