from django.shortcuts import render, HttpResponse
from .models import Teacher
# Create your views here.


def home_view(request):
    return render(request, 'teacher/teacher_view.html')

def dashboard(request):
    return render(request, 'teacher/teacher_dashboard.html')

def login(request):
    return render(request, 'teacher/teacher_login.html')

def signup(request):
    return render(request, 'teacher/teacher_signup.html')