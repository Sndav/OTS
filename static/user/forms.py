from django import forms
from captcha.fields import CaptchaField
from .models import User


class SignUpForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'nickname']


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)