from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Moderator', 'Moderator'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='User')

# Example Protected Resource
class Resource(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
