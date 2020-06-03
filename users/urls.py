from django.contrib import admin
from django.urls import path, include
from users.views import register, post_login, profile 

urlpatterns = [
    path('register/', register, name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('auth/', post_login, name = 'post_login'),
]
