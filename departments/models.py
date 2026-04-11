from django.db import models
from django.conf import settings


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    officer = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='managed_department'
    )

    def __str__(self):
        return self.name