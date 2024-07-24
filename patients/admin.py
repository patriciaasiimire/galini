from django.contrib import admin
from .models import CustomUser, PatientProfile

admin.site.register(CustomUser)
admin.site.register(PatientProfile)
