from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from main.forms import CustomUserCreationForm
from main.models import Course, Grade, Gpa
from student.models import Student
from teacher.services import CSV
from main.api import charts




def home(request):
    return render(request, 'teacher/home.html')


# @login_required
# def dashboard(request):
#     first_name = request.user.get_short_name()

#     course = Course.objects.get(teacher=request.user)
#     print(f'\n\n\n\n {course.id}, {course.title} \n\n\n\n')
#     students = Student.objects.filter(courses__id=course.id)
#     # students = Student.objects.filter(courses__title__startswith=course.title).distinct()
#     print(f'{students}\n\n\n')

#     context = {
#         'first_name': first_name,
#         'students': students
#     }

#     return render(request, 'teacher/dashboard.html', context)

class StudentListView(ListView):
    """
    Renders a list of students for a teacher.
    """
    model = Student
    template_name = 'teacher/dashboard.html'
    context_object_name = 'roster'

    def get_queryset(self):
        roster = {}
        courses = Course.objects.filter(teacher=self.request.user).all()
        for course in courses:
            students = Student.objects.filter(courses__id=course.id).all()
            roster[str(course.title)] = students

        return roster

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet
        # Get teacher name
        context['first_name'] = self.request.user.get_short_name()

        return context


class StudentDetailView(DetailView):
    model = Student

    # def get_context_data(self, **kwargs):
    # #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)

    #     context['first_name'] = self.object.user.get_short_name()

    #     # grades = Grade.objects.filter(student_id=self.object.id).all()
    #     # gpas = Gpa.objects.filter(student=self.object).all()
    #     # gpa_chart_json = charts.get_gpa_chart_data(gpas)

    #     # context['grades'] = grades
    #     # context['gpas'] = gpas
    #     # context['gpa_chart_json'] = gpa_chart_json



def upload(request):
    return render(request, 'teacher/upload.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}. You are now able to login.')
            return redirect('login')

    else:   
        form = CustomUserCreationForm
    return render(request, 'teacher/register.html', {'form':form})



# class UploadGrades()


def upload_csv(request):
    # get csv from the user
    # send it to models to parse csv and add to database
    pass



def test_csv_class(file):
    data = CSV(file)
    data.register_students()

