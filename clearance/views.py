from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ClearanceRequest, ClearanceApproval


# Create your views here.
@login_required
def student_dashboard(request):

    # make sure that only students can access
    if not hasattr(request.user, 'student'):
        return render(request, 'error.html', {'message': 'Not a student'})
    
    student = request.user.student  # Assuming a OneToOne relationship between User and Student
   
   
    # get all requests for this student
    requests = ClearanceRequest.objects.filter(student=student)
    
    # get all approvals for this student
    approvals = ClearanceApproval.objects.filter(request__student=student)

    return render(request, 'clearance/student_dashboard.html', {
        'requests': requests,
        'approvals': approvals,
    })