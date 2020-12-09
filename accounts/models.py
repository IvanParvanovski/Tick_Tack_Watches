from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    email = models.EmailField(blank=False)
    telephone_number = models.PositiveIntegerField(blank=False)
    profile_picture = models.ImageField(upload_to='users_profile_pictures')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
