from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add unique related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='therapist_customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='therapist_customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='therapist_customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='therapist_customuser'
    )

    def __str__(self):
        return self.username

class TherapistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add other fields for TherapistProfile here

    def __str__(self):
        return self.user.username
