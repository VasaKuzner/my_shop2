
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from captcha.fields import CaptchaField


from .models import *



class RegisterUserForm(UserCreationForm):
     username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
     password2 = forms.CharField(label='Повтори пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

     class Mete:
         model = User
         fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін',widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


