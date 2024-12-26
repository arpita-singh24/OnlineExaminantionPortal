from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='home'),
    path('live_exam/', views.live_exam, name='home'),
]
