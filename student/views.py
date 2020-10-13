from django.shortcuts import render
from main.models import Grade, Gpa
from main.api import charts
from student.services import get_first_name



def home(request):
    """
    Return homepage to user.
    """
    return render(request, 'student/home.html')

def dashboard(request):
    """
    Return student dashboard.
    """
    grades =Grade.objects.filter(student=request.user).all()
    first_name = get_first_name(request.user.get_short_name())
    gpas = Gpa.objects.filter(student=request.user).all()
    gpa_chart_json = charts.get_gpa_chart_data(gpas)


    context = {
        'first_name': first_name,
        'grades': grades,
        'gpas': gpas,
        'gpa_chart_json': gpa_chart_json
    }

    return render(request, 'student/dashboard.html', context)

def register(request):
    """
    Return student registration page.
    """
    return render(request, 'student/register.html')
