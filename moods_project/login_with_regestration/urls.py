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
    path('requestAdd/<int:frindId>', views.requestAdd),
    path('requestDelete/<int:frindId>', views.requestDelete),
    path('frindAdd/<int:frindId>', views.frindAdd),
    path('frindRemove/<int:frindId>', views.frindRemove),
    path('likeOnPost/<int:postId>', views.likeOnPost),
    path('changOtherId/<int:otherId>', views.changOtherId),
    path('creatMessages/<int:otherId>', views.creatMessages),
    
]
