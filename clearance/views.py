from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ClearanceRequest, ClearanceApproval


# Create your views here.
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

def officer_dashboard(request):

    # make sure that only officers can access
    if not hasattr(request.user, 'managed_department'):
        return render(request, 'error.html', {'message': 'Not an officer'})
    
    department = request.user.managed_department  # Assuming a OneToOne relationship between User and Officer
   
   
    # get all approvals for this officer
    approvals = ClearanceApproval.objects.filter(department=department)

    return render(request, 'clearance/officer_dashboard.html', {
        'approvals': approvals,
    })