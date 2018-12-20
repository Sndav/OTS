# users/adminx.py

import xadmin

from .models import *
from base.adminxBase import XadminBase


class CourseAdmin(XadminBase):
    list_display = ['name', 'students', 'click_nums', 'create_time']
    search_fields = ['name', 'desc', 'detail']
    list_filter = ['name', 'click_nums']
    style_fields = {
        "desc": "ueditor",
        "detail": "ueditor",
    }


class LessonAdmin(XadminBase):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'create_time']


class LessonDetailAdmin(XadminBase):
    list_display = ['lesson', 'detail']
    search_fields = ['lesson', 'detail']
    list_filter = ['lesson', 'detail']
    style_fields = {
        "detail": "ueditor",
    }


class LessonResourceAdmin(XadminBase):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'create_time']


class LessonNodeAdmin(XadminBase):
    list_display = ['lesson', 'user', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'user', 'create_time']


# 注册模块
xadmin.site.register(LessonNode, LessonNodeAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(LessonResource, LessonResourceAdmin)
xadmin.site.register(LessonDetail, LessonDetailAdmin)
