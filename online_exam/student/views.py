from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render(request, 'student/student_view.html')

def signup(request):
    if request.method == 'POST':
        # Fetch form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_picture = request.FILES.get('profile_picture')

        #Validate Data
        if password1 != password2:
            messages.error(request, "Password do not match!")
            return redirect('student_signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('student_signup')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "Username (email) is already taken!")
            return redirect('student_signup')
        
        # Create user and student record
        user = User.objects.create(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password1)
        )

        Student.objects.create(user=user, phone=phone, profile_picture=profile_picture)
        messages.success(request, "Registration successful!")
        return redirect('student_login')

    return render(request, 'student/student_signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful! Welcome to your dashboard.")
            return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('student_login')
        
    return render(request, 'student/student_login.html')


@login_required(login_url='student_login')
def dashboard(request):
    return render(request, 'student/student_dashboard.html')


def logout_view(request):
    logout(request)  
    messages.success(request, "Logout successful! See you soon.") 
    return redirect('student_home')  