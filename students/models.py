from django.db import models
from django.conf import settings


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.registration_number