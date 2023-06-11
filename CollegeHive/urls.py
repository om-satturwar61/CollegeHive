from django.contrib import admin
from django.urls import path, include
from CollegeHive import views

urlpatterns = [
    path("",views.home, name='home'),
    path("properties/",views.properties,name='properties'),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("properties/bharatmata-society",views.bharatmata,name='bharatmata-society'),
    path("properties/garva-girls-hostel",views.garva,name='garva-girls-hostel'),
    path("properties/guru-om-hostel",views.guruom,name='guru-om-hostel'),
    path("properties/gurukunj-hostel",views.gurukunj,name='gurukunj-hostel'),
    path("properties/harshraj-residency",views.harshraj_residency,name='harshraj-residency'),
    path("properties/mohan-villa",views.mohanvilla,name='mohan-villa'),
    path("properties/sai-glamour-residency",views.sai_glamour,name='sai-glamour-residency'),
    path("properties/saptashrungi-society",views.saptashrungi,name='saptashrungi-society'),
    path("properties/shree-ganesh-pg",views.shree_ganesh_pg,name='shree-ganesh-pg'),
    path("properties/shree-pg-services",views.shree_pg_services,name='shree-pg-services'),
    path("properties/subhadra-hostel",views.subhadra_hostel,name='subhadra-hostel')
]