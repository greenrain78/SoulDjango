from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'baekjoon_id', 'email', 'password')
