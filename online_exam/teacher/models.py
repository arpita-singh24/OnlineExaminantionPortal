from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def profile_pic_path(instance, filename):
    return f"profile_pics/{instance.user.username}/{filename}"
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
   

    def __str__(self):
        return self.user.username

