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

]
