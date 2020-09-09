from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'student/home.html')

def dashboard(request):
    return render(request, 'student/dashboard.html')

def register(request):
    return render(request, 'student/register.html')


# def profile(request):
#     return HttpResponse('<h1>Student Homepage</h1>')
