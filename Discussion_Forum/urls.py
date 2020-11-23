from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('main/', views.home,name = "main"),
    path('home/', views.home,name = "home"),
    path('addInForum/',views.forum,name = "addInForum"),
    path('addInDiscussion/',views.addInDiscussion,name="addInDiscussion"),
   
]