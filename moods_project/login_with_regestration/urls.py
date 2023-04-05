# from django.contrib import admin
from django.urls import path,include
from . import views                    # import views from current file 
urlpatterns = [
    path('login',views.show_login_page),              # here i am refering to the method
    path('',views.show_registration_page), # where the main route here is refering to the main page shown on load
    path('handle_regestration/',views.handle_regestration),
    path('handle_login/',views.handle_login),
    path('logout',views.logout),
    path('redirect',views.successfull),
    path('dashboard',views.dashboard),   # redirecting to the main dashboard after successful login
    path('user',views.logged_user_profile),    #path to show the logged user profile
    path('user/<int:user_id>', views.other_user_profile), #path to show other users profiles 
    path('likeOnPost/<int:post_id>', views.likeOnPost),
    path('add_likes_comment/<int:comment_id>',views.likeOnComemnt), 
    path('new_post',views.add_post),
    path('add-new-comment',views.add_comment),
    path('delete/<int:post_id>',views.delete_post),
    path('delete/comment/<int:comment_id>',views.delete_comment),
    path('add-friend/<int:friend_id>',views.add_friend),
    path('remove-friend/<int:friend_id>',views.remove_friend),
    path('send-request/<int:friend_id>',views.send_request),
    path('delete-request/<int:request_id>',views.delete_request),
    # path('delete-all-requests', views.delete_all_requests),
    path('accept-request/<int:request_id>/', views.accept_request),
    path('messages', views.messages),  # get all the messages 
    path('changOtherId/<int:otherId>', views.changOtherId),
    path('creatMessages/<int:otherId>', views.creatMessages),
    # path('search/<se>', views.search), #search bar
    path('search', views.search), #search bar
    path('result',views.result),
    path('edit_profile', views.editProfile),
    path('updateProfile/', views.updateProfile),
    
    
    
]
