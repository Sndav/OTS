from django import forms
from captcha.fields import CaptchaField
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'nickname']


class LoginForm(forms.Form):
    captcha = CaptchaField()
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)