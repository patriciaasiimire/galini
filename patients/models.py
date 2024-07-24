from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add unique related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='patient_customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='patient_customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='patient_customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='patient_customuser'
    )

    def __str__(self):
        return self.username

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add other fields for PatientProfile here

    def __str__(self):
        return self.user.username
