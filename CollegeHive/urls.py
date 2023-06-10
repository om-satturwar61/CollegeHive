from django.contrib import admin
from django.urls import path, include
from CollegeHive import views

urlpatterns = [
    path("",views.home, name='home'),
    path("properties/",views.properties,name='properties'),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("properties/bharatmata-society",views.bharatmata,name='bharatmata-society')
]
