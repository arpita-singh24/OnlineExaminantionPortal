from django.urls import path
from teacher import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home_view, name='teacher_view'),

    path('dashboard/', views.dashboard, name='teacher_dashboard'),
    path('signup/', views.signup, name='teacher_signup'),
    path('login/', views.login, name='teacher_login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)