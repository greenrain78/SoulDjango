# -*- coding: utf-8 -*-

import json
from urllib.parse import urlparse, parse_qs

from django.contrib import auth
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from chicken_soup.forms import UserForm
from chicken_soup.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'sign_up.html', {'form': form})


class SignUp(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'sign_up.html', {'form': form})

    def post(self, request):
        """ 일단 json을 입력받아야 하지만 프론트에서 json을 보내는 방법을 모르므로
            row데이터를 가져와서 json으로 만듬
        """
        temp = parse_qs(request.body.decode('utf-8'))
        # data = json.loads(request.body.decode('utf-8'))
        data = temp
        print(data)
        try:
            if User.objects.filter(user_name=data['user_name']).exists():
                return JsonResponse({"message": "해당 이름을 가진 유저가 이미 존재합니다."}, status=401)

            # 유저 생성
            User(
                user_name=data['user_name'][0],
                nickname=data['nickname'][0],
                baekjoon_id=data['baekjoon_id'][0],
            ).save()
            # User(
            #     user_name=data['user_name'],
            #     nickname=data['nickname'],
            #     baekjoon_id=data['baekjoon_id'],
            # ).save()
            print("저장 성공")
            # return HttpResponse(status=200)
            return redirect('/')
        except KeyError:
            return JsonResponse({'message': "잘못된 값이 입력되었습니다."}, status=400)


class UserView(View):

    # post로 유저 생성
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(user_name=data['user_name']).exists():
                return JsonResponse({"message": "USER_ALREADY_EXIST"}, status=401)

            # 유저 생성
            User(
                user_name=data['user_name'],
                nickname=data['nickname'],
                baekjoon_id=data['baekjoon_id'],
            ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)

    # 유저 조회
    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data": list(users)}, status=200)


class SignIn(View):

    def get(self, request):
        return render(request, 'sign_in.html')

    def post(self, request):
        login_email = request.POST.get('inputEmail', None)
        login_password = request.POST.get('inputPassword', None)
        user = auth.authenticate(request, useremail=login_email, password=login_password)
        print(user)
        pass


def member_list(request):
    content = {'member_list': User.objects.all()}
    return render(request, 'member_list.html', content)
