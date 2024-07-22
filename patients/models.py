from django.db import models

# Create your models here.
# patients/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
#from django.db import models

class Patient(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.username
    groups = models.ManyToManyField(
        Group,
        related_name='patient_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='patient',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='patient_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='patient',
    )
''''''
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_therapist = models.BooleanField(default=False)

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    medical_history = models.TextField()

class TherapistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    qualifications = models.TextField()
    experience = models.IntegerField() 
