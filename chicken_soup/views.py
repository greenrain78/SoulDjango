from django.shortcuts import render
from chicken_soup.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def ranking(request):
    user_list = User.objects.all()
    content = {'user_list': user_list}

    return render(request, 'ranking.html', content)


def sign_up(request):
    return render(request, 'sign_up.html')
