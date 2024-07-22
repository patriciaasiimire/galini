from django.contrib import admin
from .models import CustomUser, PatientProfile, TherapistProfile

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(PatientProfile)
admin.site.register(TherapistProfile)
#admin.site.register(Patient)