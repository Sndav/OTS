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
        upload_to='image/%Y%m',
        default='image/default.png',
        max_length=100)
    is_teacher = models.BooleanField('老师', default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class PassedCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    passed = models.TextField('通过题目', default=pickle.dumps([{}]))

    class Meta:
        verbose_name = '通过题目'
        verbose_name_plural = verbose_name


class PublishedCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    publish = models.TextField('发布题目', default=pickle.dumps([{}]))

    class Meta:
        verbose_name = '发布题目'
        verbose_name_plural = verbose_name
