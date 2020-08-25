# Teacher URLs
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='teacher-home'),
    path('dashboard', views.dashboard, name='teacher-dashboard'),
    path('upload', views.upload, name='teacher-upload'),
]
