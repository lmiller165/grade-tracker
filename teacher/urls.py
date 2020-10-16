# Teacher URLs
from django.urls import path
from .views import StudentListView, StudentDetailView
from . import views as teacher_views


urlpatterns = [
    path('', teacher_views.home, name='teacher-home'),
    path('dashboard/', StudentListView.as_view(), name='teacher-dashboard'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    # path('dashboard', teacher_views.dashboard, name='teacher-dashboard'),
    path('upload/', teacher_views.upload, name='teacher-upload'),
    path('register/', teacher_views.register, name='teacher-register')
]
