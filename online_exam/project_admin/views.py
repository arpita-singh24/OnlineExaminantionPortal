from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is home page of project")

def admin_home(request):
    return render(request, 'project_admin/admin_dashboard.html')