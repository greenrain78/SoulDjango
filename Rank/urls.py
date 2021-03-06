
from django.contrib import admin
from django.urls import path

from Rank import views

urlpatterns = [
    path('', views.rank_list, name='rank_list'),
    path('<str:user>/', views.detail, name='detail'),
    # path('list/', views.ranking, name='ranking'),
]
