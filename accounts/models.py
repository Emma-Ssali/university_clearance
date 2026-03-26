from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('officer', 'Department Officer'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    phone_number = models.CharField(max_length=15, blank=True)