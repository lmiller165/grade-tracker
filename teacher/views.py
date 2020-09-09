from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'teacher/home.html')

def dashboard(request):
    return render(request, 'teacher/dashboard.html')

def upload(request):
    return render(request, 'teacher/upload.html')

def register(request):
    return render(request, 'teacher/register.html')
