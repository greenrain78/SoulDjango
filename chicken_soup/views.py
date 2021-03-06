from django.shortcuts import render, redirect
from django.utils import timezone

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


def sign_in(request):
    return None


def member_list(request):
    return None