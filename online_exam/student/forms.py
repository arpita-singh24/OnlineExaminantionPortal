from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact = forms.CharField(max_length=15, required=True)
    profile_picture = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'contact', 'password1', 'password2', 'profile_picture']