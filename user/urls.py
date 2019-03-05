from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_view, name="user_logout"),
    path('<int:user_id>', views.InfoView.as_view(), name="userinfo"),
]
