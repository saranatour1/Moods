# 21-04-2023 updates 
from django.db import models
import datetime

# import bcrypt
# Create your models here.
import re
from dateutil.relativedelta import relativedelta
  # model maneger for the user model cas, it takes the values given from the user, and returns error if there was a problem. 
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
# Add a validate function for the update profile file. 
# User model, where the user information 
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255) # the bcrypt password hash only.
    birthday=models.DateField()
    gender = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    avatar=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManeger()

    
# Validation of the Posts,on the dashboard, on the profile, 
# on the other profile if there is a chance
class PostManager(models.Manager):
    def validate_post(self, postData):
        errors = {}
        # Validate post data
        if len(postData['post']) < 1:
            errors["post"] = "The post content cannot be empty."
        if postData['post'] =='':
            errors["post"] = "The post content cannot be empty."
        return errors
    
# Post model, the post content, likes count and users who made the post. 
class Post(models.Model):
    post_content = models.TextField() #referring to the text conent of the post
    user_who_post = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
    likes_count=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=PostManager()

    
#Commment validation, no empty comments are possible.  
class CommentManager(models.Manager):
    def validate_comment(self, postData):
        errors = {}
        # Validate post data
        if len(postData['comment']) < 1:
            errors["comment"] = "The comment content cannot be empty."
        return errors

# model class for comments on a post, which includes the comment content, user who made the comment
class Comment(models.Model):
    comment_content = models.TextField()
    user_who_comment = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments_on_post' ,on_delete=models.CASCADE)
    likes_count=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=CommentManager()    
    
    
# class for tracking likes on a post by a user, with a unique constraint to
# ensure that a user can only like a post once.
class LikePost(models.Model):
    user_who_like = models.ForeignKey(User,related_name='liked_posts', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='likes_on_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
      unique_together = ('user_who_like', 'post') # to ensure that the user likes the post only once

# Likes on comments table 
# class for tracking likes on comments, with a unique constraint to ensure that
# a user can only like a comment once.
class LikeComment(models.Model):
    user_who_like = models.ForeignKey(User,related_name='liked_comments', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,related_name='likes_on_comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
      unique_together = ('user_who_like', 'comment') # to ensure that the user likes the post only once

# friendshps table, relationships between users 
class FriendShip(models.Model):
  users = models.ManyToManyField(User,related_name='friends')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# requests table 
# class for a request with a sender, receiver, with a unique
# constraint on the sender-receiver pair.
class Request(models.Model):
    request_sender = models.ForeignKey(User,related_name='sent_requests', on_delete=models.CASCADE)
    request_reciever = models.ForeignKey(User,related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
      unique_together = ('request_sender', 'request_reciever')

# Messages table 
class OurMessage(models.Model): # i'm way to lazy to change the names :")
    user_group1 = models.ForeignKey(User,related_name='chat_groups1', on_delete=models.CASCADE,default=None)
    user_group2 = models.ForeignKey(User,related_name='chat_groups2', on_delete=models.CASCADE,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message_content = models.TextField()
    message_sender = models.ForeignKey(User,related_name='sent_messages', on_delete=models.CASCADE)
    message_receiver = models.ForeignKey(User,related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# # Randomized memes ,, randomized captions 
class Meme(models.Model):
  meme_content=models.TextField() #the meme svg
  meme_caption= models.TextField() #meme caption to that particular incedent
  status_code=models.IntegerField() #status codes only, not the whole response
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

