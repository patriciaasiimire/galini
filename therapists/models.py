from django.db import models

# Create your models here.
# therapists/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
#from django.db import models

class Therapist(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='therapist_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='therapist',
    )
    #added by me
    def _str_(self):
        return self.groups
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='therapist_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='therapist',
    )

    #added by me
    def _str_(self):
        return self.user_permissions