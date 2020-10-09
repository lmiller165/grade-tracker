from django.shortcuts import render
from main.models import Grade, Gpa
from student.services import get_first_name
import json


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

    gpa_chart_data = {
        'labels': [
            'Week 1',
            'Week 2',
            'Week 3',
            'Week 4',
            'Week 5',
            'Week 6',
            'Week 7',
            'Week 8',
            'Week 9',
            'Week 10',
            'Week 11',
            'Week 12',
            'Week 13',
            'Week 14',
            'Week 15',
            'Week 16',
            'Week 17',
            'Week 18',

        ],
        'data': [],
    }

    for gpa in gpas:
        gpa_chart_data['data'].append(gpa.gpa)

    gpa_chart_json = json.dumps(gpa_chart_data)

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
