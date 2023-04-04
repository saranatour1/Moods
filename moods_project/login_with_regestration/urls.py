# from django.contrib import admin
from django.urls import path,include
from . import views                    # import views from current file 
urlpatterns = [
    path('login',views.show_login_page),              # here i am refering to the method
    path('',views.show_registration_page), # where the main route here is refering to the main page shown on load
    path('dashboard',views.dashboard),   # redirecting to the main dashboard after successful login
    path('handle_regestration/',views.handle_regestration),
    path('handle_login/',views.handle_login),
    path('redirect',views.successfull),
    path('logout',views.logout),
    path('user',views.logged_user_profile),    #path to show the logged user profile
    path('user/<int:user_id>', views.other_user_profile), #path to show other users profiles 
    # path('requestAdd/<int:frindId>', views.requestAdd),
    # path('requestDelete/<int:frindId>', views.requestDelete),
    # path('frindAdd/<int:frindId>', views.frindAdd),
    # path('frindRemove/<int:frindId>', views.frindRemove),
    path('likeOnPost/<int:post_id>', views.likeOnPost),
    path('add_likes_comment/<int:comment_id>',views.likeOnComemnt), 
    path('new_post',views.add_post),
    path('add-new-comment',views.add_comment),
    path('delete/<int:post_id>',views.delete_post),
    path('delete/comment/<int:comment_id>',views.delete_comment),
    path('add-friend/<int:friend_id>',views.add_friend),
    path('remove-friend/<int:friend_id>',views.remove_friend),
    
]
