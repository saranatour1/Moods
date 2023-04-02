# from django.contrib import admin
from django.urls import path,include
from . import views                    # import views from current file 
urlpatterns = [
    path('',views.index),              # here i am refering to the method
                                       # where the main route here is refering to the main page shown on load
]
