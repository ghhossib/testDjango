from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин пользователя'
    )
    password = forms.CharField(
        label='пароль пользователя'
    )