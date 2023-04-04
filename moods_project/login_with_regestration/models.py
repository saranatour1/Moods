from django.db import models
import datetime

# import bcrypt
# Create your models here.
import re
from dateutil.relativedelta import relativedelta

class UserManeger(models.Manager):
    def validate_login(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #Validate regestration
        if len(postData['first_name']) < 2:
            errors["first_name"] = "the first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "the last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
          errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
          errors['password']="Password needs to be more than 8 charecters"
        if postData['confirm_password'] != postData['password']:
          errors['confirm_password']="Passwords don't match!"
        if User.objects.filter(email=postData['email']).exists():
          errors['email']="This email already exists, try login page instead"
        if postData['birthday'] > str(datetime.date.today()):
          errors["birthday"]= "You should be born in the past!"
        if postData['birthday'] == '':
          errors["birthday"] = "Please enter your birthday"
        else:
          user_birthday = datetime.datetime.strptime(postData['birthday'], '%Y-%m-%d').date()
          if user_birthday > datetime.date.today() - relativedelta(years=13):
            errors["birthday"] = "You must be at least 13 years old to register."
        return errors
  

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255) # the bcrypt password hash only.
    birthday=models.DateField()
    gender = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManeger()
    # friends : list of users

    # sent_requests : list of users
    # received_requests : list of users

    # posts : list of posts
    # liked_posts : list of posts

    # comments : list of 
    

class OurMessage(models.Model):
    user_group = models.ForeignKey(User,related_name='chat_groups', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message_content = models.TextField()
    message_sender = models.ForeignKey(User,related_name='sent_messages', on_delete=models.CASCADE)
    message_receiver = models.ForeignKey(User,related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FriendShip(models.Model):
    users = models.ManyToManyField(User,related_name='friends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Request(models.Model):
    request_sender = models.ForeignKey(User,related_name='sent_requests', on_delete=models.CASCADE)
    request_reciever = models.ForeignKey(User,related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    post_content = models.TextField()
    user_who_post = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # comments_on_post : list of comments on post
    # likes_on_post : list of likes on post


class Comment(models.Model):
    comment_content = models.TextField()
    user_who_comment = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments_on_post' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # likes_on_comment : list of likes on comment



class LikePost(models.Model):
    user_who_like = models.ForeignKey(User,related_name='liked_posts', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='likes_on_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


