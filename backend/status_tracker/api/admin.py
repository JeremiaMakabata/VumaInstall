from .models import InstallationRequest, Customer, Employee, Status
from django.contrib import admin

admin.site.register(InstallationRequest)
admin.site.register(Customer)
admin.site.register(Employee)

admin.site.register(Status)
