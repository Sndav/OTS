from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

import pickle


class User(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女'),
        ('secret', '保密')
    )

    username = models.CharField('用户名', max_length=100, unique=True)
    password = models.TextField('密码')
    nickname = models.CharField('昵称', max_length=50)
    email = models.EmailField('邮箱', max_length=50, unique=True)
    create_time = models.DateTimeField('添加时间', default=datetime.now)
    update_time = models.DateTimeField('更改时间', auto_now=True)
    gender = models.CharField(
        '性别',
        max_length=10,
        choices=gender_choices,
        default='secret')
    image = models.ImageField(
        upload_to='avatar/%Y%m%d',
        default='avatar/default.png',
        max_length=100)
    is_teacher = models.BooleanField('老师', default=False)
    desc = models.TextField("描述信息", default="暂时没有描述信息")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

