from django.contrib import admin
from .models import ClearanceRequest, ClearanceApproval


class ClearanceApprovalInline(admin.TabularInline):
    model = ClearanceApproval
    extra = 1

class ClearanceRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'date_submitted', 'status')
    inlines = [ClearanceApprovalInline]

class ClearanceApprovalAdmin(admin.ModelAdmin):
    list_display = ('request', 'department', 'approval_status')
        
# Register your models here.
admin.site.register(ClearanceRequest)
admin.site.register(ClearanceApproval)