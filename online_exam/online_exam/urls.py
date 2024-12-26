
from django.contrib import admin
from django.urls import path, include
from project_admin import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),

    path('', views.home, name='home'),
    path('admin_home', views.admin_home, name='admin_home'),
]
