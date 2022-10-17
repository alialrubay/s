from django.urls import path
from .views import *



urlpatterns = [
      path('' , home_page,name='home_page'),
     path('admin/',admin,name='admin'),
    path('pictures/' , display_pictures,name='display_pictures') ,
    path('about/' , about,name='about') ,
]