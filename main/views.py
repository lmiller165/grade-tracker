from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.api import charts

def home(request):
    return HttpResponse('<h1>Main Home</h1>')


def login_redirect(request):
    if request.user.is_teacher:
        return redirect('teacher-dashboard')
    if request.user.is_student:
        return redirect('student-dashboard')
    # TODO: check for parent views


