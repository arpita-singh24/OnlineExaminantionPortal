from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from .models import Student

# Create your views here.

def home_view(request):
    return render(request, 'student/view.html')

def dashboard(request):
    return render(request, 'student/dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            contact = form.cleaned_data.get('contact')
            profile_picture = form.cleaned_data.get('profile_picture')
            Student.objects.create(user=user, contact=contact, profile_picture=profile_picture)
            return redirect('login')
    else: 
        form = RegisterForm()
    return render(request, 'student/signup.html', {'form':form})

def login(request):
    return render(request, 'student/student_login.html')

def  student_signup(request):
    return render(request, 'student/student_register.html')