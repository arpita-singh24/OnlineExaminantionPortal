
from django.contrib import admin
from django.urls import path, include
from project_admin import views


urlpatterns = [
    #Django admin Panel
    path('admin/', admin.site.urls),

    #Including Student and Teacher Urls
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),


    # Project home Page and Admin Urls
    path('', views.home, name='home'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
]