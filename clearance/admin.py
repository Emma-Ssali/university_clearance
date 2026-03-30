from django.contrib import admin
from .models import ClearanceRequest, ClearanceApproval

# Register your models here.
admin.site.register(ClearanceRequest)
admin.site.register(ClearanceApproval)