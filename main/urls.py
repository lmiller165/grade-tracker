from django.urls import path
from . import views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_views.home, name='main-home'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('login-redirect/', main_views.login_redirect, name='login-redirect')
]