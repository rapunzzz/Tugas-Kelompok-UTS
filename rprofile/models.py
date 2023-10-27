from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    handphone = models.IntegerField()
    email = models.TextField()
  #  profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

