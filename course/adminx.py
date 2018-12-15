# users/adminx.py

import xadmin

from .models import *


# class UserAdmin(object):
#     list_display = ['id', 'username', 'email', 'gender']
#     search_fields = ['username', 'email']
#     list_filter = ['email', 'id']


# class EmailVerifyRecordAdmin(object):
#     list_display = ['id', 'code', 'email', 'send_type', 'send_time']
#     search_fields = ['email', 'send_type']
#     list_filter = ['email']
#
# xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

class CourseAdmin:
    list_display = ['name', 'students', 'click_nums', 'create_time']
    search_fields = ['name', 'desc','detail']
    list_filter = ['name', 'click_nums']


class LessonAdmin:
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'create_time']


class CourseResourceAdmin:
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'create_time']


class LessonNodeAdmin:
    list_display = ['lesson', 'user', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'user', 'create_time']


# 注册模块
xadmin.site.register(LessonNode, LessonNodeAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)