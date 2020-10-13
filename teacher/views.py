from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from main.forms import CustomUserCreationForm
from main.models import Course
from student.models import Student
from teacher.services import CSV




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
    model = Student
    template_name = 'teacher/dashboard.html'
    context_object_name = 'students'

    def get_queryset(self):
        course = Course.objects.get(teacher=self.request.user)
        students = Student.objects.filter(courses__id=course.id)
        return students

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet
        context['first_name'] = self.request.user.get_short_name()
        
        return context




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

