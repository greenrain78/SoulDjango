
from django.contrib import admin
from django.urls import path

from chicken_soup import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('list/', views.user_list, name='user_list'),
    path('', views.index, name='index'),
]
