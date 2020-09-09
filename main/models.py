from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
from django.conf import settings


class CustomUser(AbstractUser):
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


class Student(models.Model):
    RACE_CHOICES = [
        ('american_indian_or_alaska_native', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('black_or_african_american', 'Black of African American'),
        ('hispanic_or_latino', 'Hispanic or Latino'),
        ('native_hawaiian_or_pacific_islander', 'Native Hawaiin or Pacific Islander'),
        ('white', 'White')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE, null=True)
    calstudentID = models.IntegerField(max_length=None, null=True)
    is_iep = models.BooleanField(default=False, null=True)
    on_reduced_lunch = models.BooleanField(default=False, null=True)
    race = models.CharField(max_length=50, null=True, choices=RACE_CHOICES)

    def __str__(self):
        return f'{self.user} Profile'


class Course(models.Model):
    title = models.CharField(max_length=75)
    section = models.CharField(max_length=20, null=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE, null=True)
    secondary_instructor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='secondary_teacher', on_delete=models.CASCADE, null=True)
    term = models.CharField(max_length=10, null=True)
    credit_hours = models.FloatField(null=True)
    description = models.TextField(max_length=None, null=True)
    start_date = models.DateField( auto_now_add=True, null=True)
    end_date = models.DateField( auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='grades', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField()

    def __str__(self):
        return self.grade


class Gpa(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gpa', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    gpa = models.IntegerField()

    def __str__(self):
        return self.gpa