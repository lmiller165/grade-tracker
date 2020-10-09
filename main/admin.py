from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Grade, Gpa

# To create a custom view, checkout this link under the title Admin:
# https://testdriven.io/blog/django-custom-user-model/


admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Gpa)

