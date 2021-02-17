from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_list(request):
    return render(request, 'user_list.html')


def sign_up(request):
    return render(request, 'sign_up.html')
