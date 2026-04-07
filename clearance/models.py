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

    def save(self, *args, **kwargs):
        is_new = self.pk is None   # ✅ check if new request
        super().save(*args, **kwargs)

        if is_new:
            departments = Department.objects.all()
            for dept in departments:
                ClearanceApproval.objects.create(
                    request=self,
                    department=dept,
                    approval_status='Pending'
                )

    def __str__(self):
        return f"{self.student} Clearance Request"

class ClearanceApproval(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    request = models.ForeignKey(ClearanceRequest, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    approved_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        approvals = ClearanceApproval.objects.filter(request=self.request)

        # ❌ If ANY rejected → request rejected
        if approvals.filter(approval_status='Rejected').exists():
            self.request.status = 'Rejected'

        # ✅ If ALL approved → request approved
        elif approvals.filter(approval_status='Pending').count() == 0:
            self.request.status = 'Approved'

        # ⏳ Otherwise → still pending
        else:
            self.request.status = 'Pending'

        self.request.save()

    def __str__(self):
        return f"{self.department} - {self.approval_status}"