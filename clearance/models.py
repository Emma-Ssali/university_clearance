from django.db import models
from students.models import Student
from departments.models import Department

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]

# Create your models here.
class ClearanceRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.student} Clearance Request"    

class ClearanceApproval(models.Model):
    request = models.ForeignKey(ClearanceRequest, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    approved_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('request', 'department')  # 🔥 THIS LINE

    def __str__(self):
        return f"{self.department} - {self.approval_status}"