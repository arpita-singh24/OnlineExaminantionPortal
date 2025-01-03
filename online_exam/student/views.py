from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from .models import Student

# Create your views here.

def home_view(request):
    return render(request, 'student/student_view.html')

def dashboard(request):
    return render(request, 'student/student_dashboard.html')

def login(request):
    return render(request, 'student/student_login.html')

def signup(request):
    return render(request, 'student/student_signup.html')