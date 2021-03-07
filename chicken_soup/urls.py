
from django.contrib import admin
from django.urls import path

from chicken_soup import views
from chicken_soup.views import SignUp, SignIn

urlpatterns = [
    # 메인 화면
    path('', views.index, name='index'),

    # 유저 관리
    path('members/', views.member_list, name='member_list'),
    # path('signup/', views.sign_up, name='sign_up'),
    path('signup/', SignUp.as_view(), name='sign_up'),
    path('signin/', SignIn.as_view(), name='sign_in'),
    path('logout/', views.logout, name='logout'),

]
