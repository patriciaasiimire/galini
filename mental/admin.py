from django.contrib import admin
from .models import TherapistProfile, Review

admin.sites.register(TherapistProfile)
admin.sites.register(Review)