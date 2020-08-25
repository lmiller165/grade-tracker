from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Teacher Homepage</h1>')

def dashboard(request):
    return HttpResponse('<h1>Teacher Dashboard</h1>')

def upload(request):
    return HttpResponse('<h1>Teacher Upload Grades</h1>')
