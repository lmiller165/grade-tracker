# Teacher URLs
from django.urls import path
from . import views as teacher_views

urlpatterns = [
    path('', teacher_views.home, name='teacher-home'),
    path('dashboard', teacher_views.dashboard, name='teacher-dashboard'),
    path('upload', teacher_views.upload, name='teacher-upload'),
    path('register', teacher_views.register, name='teacher-register')
]
