from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ClearanceRequest, ClearanceApproval
from departments.models import Department

@receiver(post_save, sender=ClearanceRequest)
def create_clearance_approvals(sender, instance, created, **kwargs):
    if created:
        # Create a ClearanceApproval for each department
        for department in Department.objects.all():
            # ensures no duplicates
            ClearanceApproval.objects.get_or_create(
                request=instance, 
                department=department
            )