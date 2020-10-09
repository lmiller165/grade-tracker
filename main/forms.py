from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form where email is the unique identifiers
    for authentication instead of usernames.
    """
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2',]


class CustomUserChangeForm(UserChangeForm):
    """
    Custom user change form to update email.
    """
    class Meta:
        model = CustomUser
        fields = ('email',)


        