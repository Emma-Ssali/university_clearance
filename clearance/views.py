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

    # ✅ HANDLE FORM SUBMISSION
    if request.method == 'POST':
        approval_id = request.POST.get('approval_id')
        status = request.POST.get('status')

        approval = ClearanceApproval.objects.get(id=approval_id)

        # SECURITY CHECK (VERY IMPORTANT)
        if approval.department == department:
            approval.approval_status = status
            approval.approved_by = request.user
            approval.save()
        
        # NEW LOGIC STARTS HERE
        clearance_request = approval.request
        approvals = clearance_request.clearanceapproval_set.all()

        if approvals.filter(approval_status='Rejected').exists():
            clearance_request.status = 'Rejected'
        elif approvals.filter(approval_status='Pending').exists():
            clearance_request.status = 'Pending'
        else:
            clearance_request.status = 'Approved'

        clearance_request.save()
        # NEW LOGIC ENDS HERE

        return redirect('officer_dashboard')
    
    return render(request, 'clearance/officer_dashboard.html', {
        'approvals': approvals,
    })