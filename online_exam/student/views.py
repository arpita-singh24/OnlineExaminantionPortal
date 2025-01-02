from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request, 'student/student_dashboard.html')

def live_exam(request):
    return render(request, 'student/live.html')