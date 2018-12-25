"""OnlineTeachSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

import xadmin
from DjangoUeditor import urls as UeditorUrls


urlpatterns = [
    path('user/', include('user.urls')),
    path('course/', include('course.urls')),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('captcha/', include('captcha.urls')),
    path('ueditor/', include(UeditorUrls)),
]
# 静态路由
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
