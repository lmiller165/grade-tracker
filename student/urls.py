# Student URLs
from django.urls import path
from . import views as student_views


urlpatterns = [
    path('', student_views.home, name='student-home'),
    path('dashboard', student_views.dashboard, name='student-dashboard'),
    path('register', student_views.register, name='student-registration')
] 