from django.contrib import admin
from .models import ClearanceRequest, ClearanceApproval


class ClearanceApprovalInline(admin.TabularInline):
    model = ClearanceApproval
    extra = 1

class ClearanceRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'date_submitted', 'status')
    inlines = [ClearanceApprovalInline]

class ClearanceApprovalAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Admin sees everything
        if request.user.is_superuser:
            return qs

        # Officers see ONLY their department
        return qs.filter(department=request.user.department)

    def get_readonly_fields(self, request, obj=None):
        # Prevent editing other fields
        if not request.user.is_superuser:
            return ['request', 'department']
        return []

    def save_model(self, request, obj, form, change):
        obj.approved_by = request.user  # auto assign
        super().save_model(request, obj, form, change)
    
    list_display = ('request', 'department', 'approval_status')
        
# Register your models here.
admin.site.register(ClearanceRequest)
admin.site.register(ClearanceApproval)