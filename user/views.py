from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.contrib.auth.hashers import make_password

from .forms import *


class LoginView(View):
    def get(self, request):
        hashkey = CaptchaStore.generate_key()
        imageURL = captcha_image_url(hashkey)
        login_form = LoginForm()
        return render(request, 'user/login.html', {
            'login_form': login_form,
            'hashkey': hashkey,
            'image_url': imageURL

        })

    def post(self, request):
        # 实例化
        hashkey = CaptchaStore.generate_key()
        imageURL = captcha_image_url(hashkey)
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'user/login.html', {
                    'login_form': login_form,
                    'hashkey': hashkey,
                    'image_url': imageURL

                })

        else:
            return render(request, 'user/login.html', {
                'login_form': login_form,
                'hashkey': hashkey,
                'image_url': imageURL

            })


class SignUpView(View):
    def get(self, request):
        signup_form = SignUpForm()
        hashkey = CaptchaStore.generate_key()
        imageURL = captcha_image_url(hashkey)
        return render(request, 'user/register.html', {
            'signup_form': signup_form,
            'hashkey': hashkey,
            'image_url': imageURL
        })

    def post(self, request):
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('/user/login')
        else:
            hashkey = CaptchaStore.generate_key()
            imageURL = captcha_image_url(hashkey)
            return render(request, 'user/register.html', {
                'signup_form': register_form,
                'hashkey': hashkey,
                'image_url': imageURL
            })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')