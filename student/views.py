from django.shortcuts import render
from main.models import Grade, Gpa, Course
from main.api import charts
from student.services import get_first_name
import datetime



def home(request):
    """
    Return homepage to user.
    """
    return render(request, 'student/home.html')
    

def dashboard(request):
    """
    Return student dashboard.
    """
    gpas = Gpa.objects.filter(student=request.user).all()
    gpa_chart_json = charts.get_gpa_chart_data(gpas)
    latest_class_avgs = {}

    courses = Course.objects.filter(student=request.user.student).all()

    for course in courses:
        grade = Grade.objects.filter(course=course).latest('timestamp')
        latest_class_avgs[course.title] = grade.grade

    context = {
        'gpa_chart_json': gpa_chart_json,
        'latest_class_avgs': latest_class_avgs
    }

    return render(request, 'student/dashboard.html', context)


def register(request):
    """
    Return student registration page.
    """
    return render(request, 'student/register.html')
