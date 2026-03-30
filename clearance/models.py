from django.db import models
from students.models import Student
from departments.models import Department

# Create your models here.
class ClearanceRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

class ClearanceApproval(models.Model):
    request = models.ForeignKey(ClearanceRequest, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=20, default='Pending')
    comments = models.TextField(blank=True)