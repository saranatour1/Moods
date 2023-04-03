from django.db import models




class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # email = models.CharField(max_length=255, unique=True)
    # password_hash = models.CharField(max_length=255) # the bcrypt password hash only.
    # birthday=models.DateField()
    # gender = models.BooleanField()
    # time_zone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # friends : list of users

    # sent_requests : list of users
    # received_requests : list of users

    # posts : list of posts
    # liked_posts : list of posts

    # comments : list of comments
    # //////////////////////////liked_comments : list of comments

    # sent_messages : list of sent messages
    # received_messages : list of received messages




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


class FriendShip(models.Model):
    users = models.ManyToManyField(User,related_name='friends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class LikePost(models.Model):
    user_who_like = models.ForeignKey(User,related_name='liked_posts', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='likes_on_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class LikeComment(models.Model):
#     user_who_like = models.ForeignKey(User,related_name='liked_comments', on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment,related_name='likes_on_comment',on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    message_content = models.TextField()
    message_sender = models.ForeignKey(User,related_name='sent_messages', on_delete=models.CASCADE)
    message_receiver = models.ForeignKey(User,related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Request(models.Model):
    request_sender = models.ForeignKey(User,related_name='sent_requests', on_delete=models.CASCADE)
    request_reciever = models.ForeignKey(User,related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)