from django.contrib import admin
from .models import CustomUser, TherapistProfile

admin.site.register(CustomUser)
admin.site.register(TherapistProfile)
