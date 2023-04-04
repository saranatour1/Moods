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


def logout(request):
  request.session.flush()
  return redirect('/')



# The main dashboard page at route  /dashboard 
def dashboard(request):
    user_id=request.session['newUser']
    newUser=User.objects.get(id=user_id)
    user_age= datetime.date.today()- newUser.birthday 
    age= (user_age.days//365)
    time_zone=newUser.time_zone
    current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
    current_time_str = current_time.strftime('%H:%M:%S')
    current_date_str = current_time.strftime('%Y-%m-%d')
    posts = Post.objects.all().order_by("-created_at")
    for post in posts:
        comments = post.comments_on_post.all().order_by("-created_at")
        post.all_comments = comments
        post.likes_count = post.likes_on_post.count() 

    # checking if the user has like the post 
    
    
    context= {
        'newUser':newUser,
        'user_age':age,
        'current_time':current_time_str,
        'current_date':current_date_str,
        'all_posts':posts,
    }
    return render(request,"dashboard.html",context)


# adding a post functionality 

def add_post(request):
  if request.method=='POST':
      errors=Post.objects.validate_post(request.POST)
      if len(errors) > 0:
          error_list = []
          for key, value in errors.items():
              error_list.append(value)
          return JsonResponse({'success': False, 'errors': error_list}) #removed the redirection 
      else:
        user_id=request.session['newUser']
        logged_user = User.objects.get(id=user_id)
        Post.objects.create(post_content=request.POST['post'], user_who_post=logged_user)
        # return JsonResponse({'success': True})
  return redirect('/dashboard')

# deleting a post 
def delete_post(request,post_id):
  user_id=request.session['newUser']
  logged_user = User.objects.get(id=user_id)
  post_object = Post.objects.get(id=post_id)
  if logged_user == post_object.user_who_post:
      post_object.delete()
  return redirect('/dashboard')

# adding a comment to that post
def add_comment(request):
    if request.method == 'POST':
        user_id=request.session['newUser']
        logged_user = User.objects.get(id=user_id)
        post_object = Post.objects.get(id=request.POST['post_id'])
        Comment.objects.create(comment_content=request.POST['comment'], user_who_comment=logged_user,post=post_object)
    return redirect('/dashboard')
  
# delete comment
def delete_comment(request,comment_id):
  user_id=request.session['newUser']
  logged_user = User.objects.get(id=user_id)
  comment_object = Comment.objects.get(id=comment_id)
  if logged_user == comment_object.user_who_comment:
      comment_object.delete()
  return redirect('/dashboard')

# adding likes to posts
def likeOnPost(request, post_id):
    user = User.objects.get(id=request.session['newUser'])
    post = Post.objects.get(id=post_id)
    like_exists = LikePost.objects.filter(user_who_like=user, post=post).exists()
    if like_exists:
        like = LikePost.objects.get(user_who_like=user, post=post)
        like.delete()
        post.likes_count -= 1
        post.save()
    else:
        LikePost.objects.create(user_who_like=user, post=post)
        post.likes_count += 1
        post.save()
    return redirect('/dashboard')
  
# adding likes to comments 
def likeOnComemnt(request,comment_id):
    user = User.objects.get(id=request.session['newUser'])
    comment = Comment.objects.get(id=comment_id)
    like_exists = LikeComment.objects.filter(user_who_like=user, comment=comment).exists()
    if like_exists:
        like = LikeComment.objects.get(user_who_like=user, comment=comment)
        like.delete()
        comment.likes_count -= 1
        comment.save()
    else:
        LikeComment.objects.create(user_who_like=user, comment=comment)
        comment.likes_count += 1
        comment.save()
    return redirect('/dashboard')







# def requestAdd(request,frindId):
#     sender = User.objects.get(id = request.session['id'])
#     reciever = User.objects.get(id = int(frindId))
#     Request.objects.create(request_sender = sender,request_reciever = reciever )
#     return redirect('/dashboard') 


# def requestDelete(request,frindId):
#     user = User.objects.get(id = request.session['id'])
#     other = User.objects.get(id = int(frindId))
#     user.sent_requests.delete(other)
#     user.received_requests.delete(other)
#     return redirect('/dashboard') 

# def frindAdd(request,frindId):
#     user = User.objects.get(id = request.session['id'])
#     friend = User.objects.get(id = int(frindId))
#     user.friends.add(friend)
#     return redirect('/dashboard') 

# def frindRemove(request,frindId):
#     user = User.objects.get(id = request.session['id'])
#     friend = User.objects.get(id = int(frindId))
#     user.friends.remove(friend)
#     return redirect('/dashboard') 











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