from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views import View

from .forms import *


class LoginView(View):
    def get(self,request):
        return render(request, 'user/login.html')

    def post(self, request):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # 登录
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'user/login.html', {'msg': '用户名或密码错误', 'login_form': login_form})

        else:
            return render(request, 'user/login.html', {'login_form': login_form})


class SignUpView(View):
    def get(self, request):
        signup_form = SignUpForm()
        return render(request, 'user/register.html', {'signup_form': signup_form})

    def post(self, request):
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', None)
            # 如果用户已存在，则提示错误信息
            if User.objects.filter(email=email):
                return render(request, 'user/register.html', {'signup_form': register_form, 'msg': '用户已存在'})
            register_form.save()
            return HttpResponseRedirect('/user/login')
        else:
            return render(request, 'user/register.html', {'signup_form': register_form})