# users/adminx.py

import xadmin
from xadmin import views

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

class PublishedCourseAdmin:
    list_display = ['user', 'publish']
    search_fields = ['user', 'publish']
    list_filter = ['user']


class BaseSetting(object):  # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object): # 全局修改，固定写法
    # 修改title
    site_title = 'XXX'
    # 修改footer
    site_footer = 'XXX'
    # 收起菜单
    menu_style = 'accordion'


# 注册模块
xadmin.site.register(PublishedCourse, PublishedCourseAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
