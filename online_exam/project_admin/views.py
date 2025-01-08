from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'project_admin/home.html')

def admin_login(request):
    return render(request, 'project_admin/admin_login.html')

def admin_dashboard(request):
    return render(request, 'project_admin/admin_dashboard.html')
