from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'email']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
