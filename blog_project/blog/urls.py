from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.home, name='home'),
    path('details',views.details, name='details'),
    path('profile',views.profile, name='modify'),
    path('register',views.register, name='register'),
    path('contact',views.contact, name='contact')
]