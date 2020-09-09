# Student URLs
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('dashboard', views.dashboard, name='student-dashboard'),
    path('register', views.register, name='student-registration')
]