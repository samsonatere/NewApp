from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=False)
    role = models.CharField(max_length=20, null=True, blank=True)
    image = CloudinaryField(default="profile1.png", null=True, blank=True)