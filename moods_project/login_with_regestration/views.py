from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import JsonResponse, HttpRequest
from pytz import all_timezones  # importing all time zones in the pyz library
from .models import *

# Create your views here.
import pytz
import bcrypt

# from datetime import datetime
import datetime

# referring to the main login method
def show_login_page(request):
    return render(request, "login.html ")


# referring to the main regestration page
def show_registration_page(request):
    time_zones = all_timezones
    context = {"time_zones": time_zones}
    return render(request, "register.html", context)


# create a new user object where the values are handles as form data
def handle_regestration(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            error_list = []
            for key, value in errors.items():
                error_list.append(value)
            return JsonResponse(
                {"success": False, "errors": error_list}
            )  # removed the redirection
        else:
            password = request.POST["password"]
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                birthday=request.POST["birthday"],
                gender=request.POST["gender"],
                time_zone=request.POST["time_zone"],
                password_hash=pw_hash,
            )
            newUser = User.objects.last().id
            request.session["newUser"] = newUser
            # return redirect('/dashboard')
            return JsonResponse(
                {"success": True}
            )  # returned true instead of redirection
    else:
        return redirect("/")


# Making the logged user log in to the wall app not to the success page
def successfull(request):
    if "newUser" in request.session:
        return redirect("/dashboard")
    else:
        return redirect("/")


# route to handle login


def handle_login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST["email"]).first()
        if user:
            if bcrypt.checkpw(
                request.POST["password"].encode(), user.password_hash.encode()
            ):
                request.session["newUser"] = user.id
                return JsonResponse({"success": True})
            else:
                return JsonResponse(
                    {"success": False, "errors": ["Invalid email or password"]}
                )
        else:
            return JsonResponse(
                {"success": False, "errors": ["Invalid email or password"]}
            )
    return JsonResponse({"success": False, "errors": ["please try again"]})


def logout(request):
    request.session.flush()
    return redirect("/")


# The main dashboard page at route  /dashboard
def dashboard(request):
    user_id = request.session["newUser"]
    newUser = User.objects.get(id=user_id)
    user_age = datetime.date.today() - newUser.birthday
    age = user_age.days // 365
    time_zone = newUser.time_zone
    current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
    current_time_str = current_time.strftime("%H:%M:%S")
    current_date_str = current_time.strftime("%Y-%m-%d")
    posts = Post.objects.all().order_by("-created_at")
    for post in posts:
        comments = post.comments_on_post.all().order_by("-created_at")
        post.all_comments = comments
        post.likes_count = post.likes_on_post.count()

    # checking if the user has like the post
    context = {
        "newUser": newUser,
        "user_age": age,
        "current_time": current_time_str,
        "current_date": current_date_str,
        "all_posts": posts,
    }
    return render(request, "dashboard.html", context)


# adding a post functionality


def add_post(request):
    if request.method == "POST":
        errors = Post.objects.validate_post(request.POST)
        if len(errors) > 0:
            error_list = []
            for key, value in errors.items():
                error_list.append(value)
            return JsonResponse(
                {"success": False, "errors": error_list}
            )  # removed the redirection
        else:
            user_id = request.session["newUser"]
            logged_user = User.objects.get(id=user_id)
            Post.objects.create(
                post_content=request.POST["post"], user_who_post=logged_user
            )
    return JsonResponse({"success": True})
    # return redirect('/dashboard')


# deleting a post
def delete_post(request, post_id):
    user_id = request.session["newUser"]
    logged_user = User.objects.get(id=user_id)
    post_object = Post.objects.get(id=post_id)
    if logged_user == post_object.user_who_post:
        post_object.delete()
    return redirect("/dashboard")


# adding a comment to that post
def add_comment(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        if post_id is None:
            return JsonResponse({"success": False, "errors": ["Post ID is missing"]})
        errors = Comment.objects.validate_comment(request.POST)
        if len(errors) > 0:
            error_list = []
            for key, value in errors.items():
                error_list.append(value)
            return JsonResponse({"success": False, "errors": error_list})
        else:
            user_id = request.session["newUser"]
            logged_user = User.objects.get(id=user_id)
            post_object = Post.objects.get(id=post_id)
            Comment.objects.create(
                comment_content=request.POST["comment"],
                user_who_comment=logged_user,
                post=post_object,
            )
    return JsonResponse({"success": True})
    # return redirect('/dashboard')


# delete comment
def delete_comment(request, comment_id):
    user_id = request.session["newUser"]
    logged_user = User.objects.get(id=user_id)
    comment_object = Comment.objects.get(id=comment_id)
    if logged_user == comment_object.user_who_comment:
        comment_object.delete()
    return redirect("/dashboard")


def likeOnPost(request, post_id):
    user = User.objects.get(id=request.session["newUser"])
    post = Post.objects.get(id=post_id)
    like_exists = LikePost.objects.filter(user_who_like=user, post=post).exists()
    if like_exists:
        like = LikePost.objects.get(user_who_like=user, post=post)
        like.delete()
        post.likes_count -= 1
    else:
        LikePost.objects.create(user_who_like=user, post=post)
        post.likes_count += 1
    post.save()
    return JsonResponse(
        {"likes_count": post.likes_count}
    )  # this is instantanously updating which is what we are looking for


# check the comment on the .html


# adding likes to comments
def likeOnComemnt(request, comment_id):
    user = User.objects.get(id=request.session["newUser"])
    comment = Comment.objects.get(id=comment_id)
    like_exists = LikeComment.objects.filter(
        user_who_like=user, comment=comment
    ).exists()
    if like_exists:
        like = LikeComment.objects.get(user_who_like=user, comment=comment)
        like.delete()
        comment.likes_count -= 1
        comment.save()
    else:
        LikeComment.objects.create(user_who_like=user, comment=comment)
        comment.likes_count += 1
        comment.save()
    return JsonResponse({"likes_count": comment.likes_count})


# the logged in user profile, showing the friendships, and all the neccessary functionalities

# the functionality here is really simple, accept or delete requests for only the logged user,
# have the friends of this user be displayed
# display the user posts


def logged_user_profile(request):
    if "newUser" in request.session:
        user_id = request.session["newUser"]
        newUser = User.objects.get(id=user_id)
        user_age = datetime.date.today() - newUser.birthday
        age = user_age.days // 365
        time_zone = newUser.time_zone
        current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
        current_time_str = current_time.strftime("%H:%M:%S")
        current_date_str = current_time.strftime("%Y-%m-%d")
        posts = Post.objects.filter(user_who_post=user_id).order_by("-created_at")

        # All the user friends
        friends = newUser.friends.all()
        friend_count = newUser.friends.count()

        # Get all the requests where the logged user is the receiver
        requests = Request.objects.filter(request_reciever=newUser).all()
        requests_count = newUser.received_requests.count()
        print(requests_count)
        for friend_request in requests:
            sender = friend_request.request_sender
            print(sender)
        
        context = {
            "newUser": newUser,
            "user_age": age,
            "current_time": current_time_str,
            "current_date": current_date_str,
            "all_posts": posts,
            "all_friends": friends,
            "friends_count": friend_count,
            "all_requests": requests,
            "friend_request_count": requests_count,
        }
        return render(request, "userprofile.html", context)


# friend requests
# How to think:
# as a person who is looking at other peoples profiles, I send them friend requests
# they recieve the friend request, after that , they become the logged in user
# they are met with the fact that they now hove a request in their main profile
# if they accept we become friends else the request is removed and the friendship is not added
# where to start? friendships
# for demonstration purposes, I addded friendships in the shell :)
# friend 1 added to 2
# friend 1 added to 3
# friend 1 added to 4

# Note: this is in the other user profiles
# handling adding or sending friend requests:
# I am the other user who's accepting the request

# the rendered user profile page
# other users profile
# the friendships are done
# onto the requests


def other_user_profile(request, user_id):
    logged_user_id = request.session.get("newUser")
    if not logged_user_id:
        return redirect("/login")

    if user_id == logged_user_id:
        return redirect("/user")

    logged_user = User.objects.filter(id=logged_user_id).first()
    if not logged_user:
        return redirect("/login")

    is_friend = (
        FriendShip.objects.filter(users=logged_user).filter(users__id=user_id).exists()
    )

    outgoing_request = Request.objects.filter(
        request_sender=logged_user, request_reciever__id=user_id
    ).first()

    incoming_request = Request.objects.filter(
        request_sender__id=user_id, request_reciever=logged_user
    ).first()

    has_a_request = Request.objects.filter(
        request_sender__id=user_id, request_reciever=logged_user
    ).exists()

    user = User.objects.filter(id=user_id).first()
    if not user:
        return redirect("/user")

    user_age = datetime.date.today() - user.birthday
    age = user_age.days // 365
    time_zone = user.time_zone
    current_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone))
    current_time_str = current_time.strftime("%H:%M:%S")
    current_date_str = current_time.strftime("%Y-%m-%d")

    # for the logged in user
    time_zone_logged = logged_user.time_zone
    current_time_logged = datetime.datetime.now(pytz.utc).astimezone(
        pytz.timezone(time_zone_logged)
    )
    # Hourly time difference
    time_difference = current_time_logged - current_time
    # time_difference_in_hours = int(abs(time_difference.total_hours() / 3600))
    print(time_difference)
    # if time_difference.total_seconds() > 0:
    #   msg=f"<p> You are {time_difference_in_hours} ahead</p>"
    # elif time_difference.total_seconds() == 0:
    #   msg="<p> You have the same time  </p>"
    #   # time_difference_in_hours=abs(time_difference_in_hours)
    # else:
    #   msg=f"<p> You are {time_difference_in_hours} behind </p>"

    context = {
        "newUser": logged_user,
        "user": user,
        "user_age": age,
        "current_time": current_time_str,
        "current_date": current_date_str,
        "outgoing_request": outgoing_request,
        "incoming_request": incoming_request,
        "is_friend": is_friend,
        "has_a_request": has_a_request,
        # 'msg':msg,
    }

    return render(request, "otheruserprofile.html", context)


# Create a friendships instance
def add_friend(request, friend_id):
    request_sender = User.objects.get(id=request.session["newUser"])
    friend_to_be_added = User.objects.get(id=int(friend_id))

    # Check if the friendship already exists
    if (
        FriendShip.objects.filter(users=request_sender)
        .filter(users=friend_to_be_added)
        .exists()
    ):
        return redirect(f"/user/{friend_id}")

    # Check if there is a pending request
    pending_request = Request.objects.filter(
        request_sender=request_sender, request_reciever=friend_to_be_added
    ).first()
    if pending_request:
        friendship = FriendShip.objects.create()
        friendship.users.add(request_sender)
        friendship.users.add(friend_to_be_added)
        request_sender.friends.add(friendship)
        pending_request.delete()
    else:
        Request.objects.create(
            request_sender=request_sender, request_reciever=friend_to_be_added
        )

    return redirect(f"/user/{friend_id}")


def remove_friend(request, friend_id):
    request_sender = User.objects.get(id=request.session["newUser"])
    friend_to_be_removed = User.objects.get(id=int(friend_id))

    friendship = (
        FriendShip.objects.filter(users=request_sender)
        .filter(users=friend_to_be_removed)
        .first()
    )

    # Remove the Friendship instance if it exists
    if friendship:
        request_sender.friends.remove(friendship)
    return redirect(f"/user/{friend_id}")


# jumping to requests
# Sending  a request
def send_request(request, friend_id):
    sender = User.objects.get(
        id=request.session["newUser"]
    )  # I am the one who sent the request
    receiver = User.objects.get(id=int(friend_id))

    # check if the sender and receiver are already friends
    if FriendShip.objects.filter(users=sender).filter(users=receiver).exists():
        return redirect(f"/user/{friend_id}")

    # check if a request already exists
    if Request.objects.filter(
        request_sender=sender, request_reciever=receiver
    ).exists():
        return redirect(f"/user/{friend_id}")

    # check if there is an incoming request from the receiver to the sender
    incoming_request = Request.objects.filter(
        request_sender=receiver, request_reciever=sender
    ).first()
    if incoming_request:
        friendship = FriendShip.objects.create()
        friendship.users.add(sender)
        friendship.users.add(receiver)
        sender.friends.add(friendship)
        incoming_request.delete()
        return redirect(f"/user/{friend_id}")

    # create a new request
    Request.objects.create(request_sender=sender, request_reciever=receiver)
    return redirect(f"/user/{friend_id}")


# accept request
def accept_request(request, request_id):
    # Get the request object
    friend_request = Request.objects.get(id=request_id)
    user = User.objects.get(
        id=request.session["newUser"]
    )  # I am the one who accepts the request

    friend_ship = FriendShip.objects.create()
    friend_ship.users.add(friend_request.request_sender)
    friend_ship.users.add(int(user.id))
    friend_ship.save()
    old_friend_id = friend_request.request_sender.id
    friend_request.delete()
    return redirect(f"/user/{old_friend_id}")


# not needed!
def delete_request(request, request_id):
    # if the person is allready a friend, do nothing, if not and ignore is pressed just remove the request
    request_to_ignore = Request.objects.get(id=request_id)
    request_to_ignore.delete()
    return redirect("/user")


# def delete_all_requests(request):
#     Request.objects.all().delete()
#     FriendShip.objects.all().delete()
#     return redirect("/user")

# adding the messages page:


# # def messages(request):
#   if 'otherId' not in request.session :
#     if User.objects.last().id:
#         otherId = User.objects.last().id
#         request.session['otherId'] = otherId
#         return redirect('/messages')
#     else:
#       user_id = request.session["newUser"]
#       newUser = User.objects.get(id=user_id)
#       user_age = datetime.date.today() - newUser.birthday
#       age = user_age.days // 365
#       time_zone = newUser.time_zone
#       current_time = datetime.datetime.now(pytz.utc).astimezone(
#           pytz.timezone(time_zone)
#       )
#       current_time_str = current_time.strftime("%H:%M:%S")
#       current_date_str = current_time.strftime("%Y-%m-%d")
        
#       all_users = User.objects.all()
#       context = {
#           "theUser": newUser,
#           "user_age": age,
#           "current_time": current_time_str,
#           "current_date": current_date_str,
#           "all_users":all_users,
#       }
#     return render(request,'messages1.html',context)
#   else:
#         user_id = request.session["newUser"]
#         newUser = User.objects.get(id=user_id)
#         all_users = User.objects.all()
#         # --------------------------
#         user = User.objects.get(id=user_id)  # the logged in user
#         other = User.objects.get(
#             id=request.session["otherId"]
#         )  # the other user i am sending a mesaage to
#         sent = Message.objects.filter(message_receiver=other, message_sender=user)
#         received = Message.objects.filter(message_sender=other, message_receiver=user)
#         allSR = received.union(sent)  # all the messages

#         userId = request.session["newUser"]
#         messages = Message.objects.all().order_by("-created_at")
#         arrI = []
#         arrP = []
#         all_users_for_last_messages = []
#         for message in messages:
#             if message.message_sender_id == userId and userId not in arrI:
#                 arrI.append(message.message_receiver_id)
#                 arrP.append(1)
#             elif message.message_receiver_id == userId and userId not in arrI:
#                 arrI.append(message.message_sender_id)
#                 arrP.append(0)
#         for i in range(len(arrI)):
#             if User.objects.get(id=arrI[i]) not in all_users_for_last_messages:
#                 all_users_for_last_messages.append(User.objects.get(id=arrI[i]))

#         # the other user details
#         user_age = datetime.date.today() - other.birthday
#         age = user_age.days // 365
#         time_zone = other.time_zone
#         current_time = datetime.datetime.now(pytz.utc).astimezone(
#             pytz.timezone(time_zone)
#         )
#         current_time_str = current_time.strftime("%H:%M:%S")
#         current_date_str = current_time.strftime("%Y-%m-%d")

#         # for the logged in user
#         # time_zone_logged = logged_user.time_zone
#         # current_time_logged = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone(time_zone_logged))
#         # # Hourly time difference
#         # time_difference = current_time_logged - current_time
#         # # time_difference_in_hours = int(abs(time_difference.total_hours() / 3600))
#         # print(time_difference)
#         context = {
#             "allSR": allSR,
#             "all_users_for_last_messages": all_users_for_last_messages,
#             "all_users": all_users,
#             "sent": sent,
#             "received": received,
#             "other": other,
#             "theUser": User.objects.get(
#                 id=request.session["newUser"]
#             ),  # need to remove this, repititive
#             "newUser": newUser,
#             "user_age": age,
#             "current_time": current_time_str,
#             "current_date": current_date_str,
#         }
#         return render(request, "messages.html", context)

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
        


        request.session['id']=request.session['newUser']

        all_users = User.objects.all() 
        # --------------------------
        user = User.objects.get(id = request.session['id'])
        other = User.objects.get(id=request.session['otherId'])



        sent = Message.objects.filter(message_receiver = other,message_sender = user)
        
        received = Message.objects.filter(message_sender = other,message_receiver = user)
        
        allSR = received.union(sent)  # messagess

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
                
 

        context = {
                'allSR': allSR,
                'all_users_for_last_messages': all_users_for_last_messages,
                'all_users' : all_users,
                'sent': sent,
                'received' : received,
                'other':other,
                'theUser' : User.objects.get(id = request.session['id']),
                'newUser':newUser,
                'user_age':age,
                'current_time':current_time_str,
                'current_date':current_date_str, 
                }
        return render(request,'messages.html',context)



# this can be removed
def changOtherId(request, otherId):
    request.session["otherId"] = otherId
    return redirect("/messages")

# function to create a message
def creatMessages(request, otherId):
    message_content = request.POST["message_content"]
    message_sender = User.objects.get(id=request.session["newUser"])
    message_receiver = User.objects.get(id=int(otherId))
    Message.objects.create(
        message_content=message_content,
        message_sender=message_sender,
        message_receiver=message_receiver,
    )
    # message_sender.chat_groups.add(message_receiver)
    OurMessage.objects.create(user_group1=message_sender, user_group2=message_receiver)
    return redirect("/messages")


