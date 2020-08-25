from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Student Homepage</h1>')

def profile(request):
    return HttpResponse('<h1>Student Homepage</h1>')
