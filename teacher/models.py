from django.db import models
from django.conf import settings

class Teacher(models.Model):
    """
    Teacher model stores all information that is unique to teachers.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE, null=True)
    profile_img = models.ImageField(default='default.jpg', upload_to='profile_imgs')

    def __str__(self):
        return f'{self.user} Profile'