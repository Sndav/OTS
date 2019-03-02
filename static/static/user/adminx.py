# users/adminx.py

import xadmin
from xadmin import views

from .models import *
from base.adminxBase import XadminBase


class PublishedCourseAdmin(XadminBase):
    list_display = ['user', 'publish']
    search_fields = ['user', 'publish']
    list_filter = ['user']


class BaseSetting(XadminBase):  # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(XadminBase):  # 全局修改，固定写法
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