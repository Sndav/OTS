# users/adminx.py

import xadmin
from xadmin import views

from .models import *
from base.adminxBase import XadminBase


class BaseSetting(XadminBase):  # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(XadminBase):  # 全局修改，固定写法
    # 修改title
    site_title = 'IoTeach'
    # 修改footer
    site_footer = 'IoTeach'
    # 收起菜单
    menu_style = 'accordion'


# 注册模块
xadmin.site.register(views.CommAdminView, GlobalSettings)
