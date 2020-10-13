from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.forms import CustomUserCreationForm
from teacher.services import CSV



def home(request):
    return render(request, 'teacher/home.html')


@login_required
def dashboard(request):
    first_name = request.user.get_short_name()
    
    return render(request, 'teacher/dashboard.html', {'first_name': first_name})


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

