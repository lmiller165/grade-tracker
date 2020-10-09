from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    """
    Custom user model that handles 3 user types using bool.
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Course(models.Model):
    """
    Course model stores information for each course, including the teacher and optional co-teacher.
    """
    title = models.CharField(max_length=75)
    section = models.CharField(max_length=20, null=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='course_teacher', on_delete=models.CASCADE, null=True)
    secondary_instructor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='secondary_teacher', on_delete=models.CASCADE, blank=True, null=True)
    term = models.CharField(max_length=10, null=True, blank=True)
    credit_hours = models.FloatField(null=True)
    description = models.TextField(max_length=None, null=True, blank=True)
    start_date = models.DateField( auto_now_add=True, null=True)
    end_date = models.DateField( auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    """
    Grade model will store every grade for each student. 
    """
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='grades', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField()

    def __str__(self):
        return f'{self.student.get_full_name()}: {self.grade}'


class Gpa(models.Model):
    """
    GPA model may be removed if GPA will be calculated rather than stored.
    """
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gpa', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    gpa = models.FloatField()

    def __str__(self):
        return f'{self.student.get_full_name()}: {self.gpa}'



