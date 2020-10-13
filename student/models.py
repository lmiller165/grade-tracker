from django.db import models
from django.conf import settings
from main.models import Course

class Student(models.Model):
    """
    Student model stores all information that is unique to students.
    """
    RACE_CHOICES = [
        ('american_indian_or_alaska_native', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('black', 'Black'),
        ('latinx', 'Latinx'),
        ('native_hawaiian_or_pacific_islander', 'Native Hawaiin or Pacific Islander'),
        ('white', 'White'),
        ('other', 'Other')
    ]

    ELL_CHOICES = [
        ('EO', 'EO'),
        ('EL', 'EL'),
        ('RFEP', 'RFEP'),
        ('IFEP', 'IFEP'),
        ('N/A', 'N/A')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE, null=True)
    grade_level = models.IntegerField(max_length=None, null=True) 
    profile_img = models.ImageField(default='default.jpg', upload_to='profile_imgs')
    calstudentID = models.IntegerField(max_length=None, null=True)
    is_iep = models.BooleanField(default=False, null=True) # The IEP, Individualized Education Program,
    ell_status = models.CharField(max_length=50, null=True, choices=ELL_CHOICES) #ELL, English Language Learner
    on_reduced_lunch = models.BooleanField(default=False, null=True) #Some students who qualify for reduced lunch
    race = models.CharField(max_length=50, null=True, choices=RACE_CHOICES)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.user} Profile'

    def create_new_student(self):
        pass