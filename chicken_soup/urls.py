
from django.contrib import admin
from django.urls import path

from chicken_soup import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking/', views.ranking, name='ranking'),
    path('signup/', views.sign_up, name='sign_up'),

]
