from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ClearanceRequest, ClearanceApproval


# Create your views here.
@login_required
def student_dashboard(request):
    student = request.user.student

    requests = ClearanceRequest.objects.filter(student=student)
    approvals = ClearanceApproval.objects.filter(request__student=student)

    return render(request, 'clearance/student_dashboard.html', {
        'requests': requests,
        'approvals': approvals,
    })