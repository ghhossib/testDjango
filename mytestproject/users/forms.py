from distutils.command.clean import clean

from django import forms
from django.contrib.auth import authenticate

from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'например User',
                'id': "email"
            }
        )
    )
    password = forms.CharField(
        label='пароль пользователя',
        widget = forms.TextInput(
             attrs={
            'class': 'form-control',
            'placeholder': 'например пароль',
            'id': "email"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user = authenticate(username=username,
                                     password=password)
            if self.user is not None or self.user.is_active:
                return self.user
            else:
                return None
        return cleaned_data