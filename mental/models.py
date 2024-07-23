from django.db import models
from django.contrib.auth.models import User
import datetime


class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='therapist_profiles/', blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    languages_spoken = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.specialization}'

class Review(models.Model):
    therapist = models.ForeignKey(TherapistProfile, related_name='reviews', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.therapist.first_name} by {self.patient.username}'
