# from django.contrib import admin
from django.urls import path,include
from .views import *
app_name = 'signupin'
urlpatterns = [
    path('', review, name = 'review'),
    path('signup/', signup, name='signup'),  
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),  
    path('profile/', profile, name='profile'),  
]