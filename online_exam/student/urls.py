from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_view, name='student_home'),
    path('signup/', views.signup, name='student_signup'),
    path('login/', views.login, name='student_login'),
    path('dashboard/', views.dashboard, name='student_dashboard'),
    path('logout/', views.logout_view, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)