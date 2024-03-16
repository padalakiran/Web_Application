from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_page', views.home, name='home'),
    path('data_page', views.data, name='data'),
    path('datas', views.datas, name='datas'),
    path('save', views.click, name='save'),
]
