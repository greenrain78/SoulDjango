
from django.contrib import admin
from django.urls import path

from chicken_soup import views

urlpatterns = [
    # 메인 화면
    path('', views.index, name='index'),

    # 유저 관리
    path('member/', views.member_list, name='member_list'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),

]
