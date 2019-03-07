# users/adminx.py

import xadmin

from .models import *
from base.adminxBase import XadminBase


class LinkAdmin(XadminBase):
    list_display = ['user', 'course', 'status', 'detail_status']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course']


# 注册模块
xadmin.site.register(Link, LinkAdmin)
