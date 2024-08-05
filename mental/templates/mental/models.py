from django.db import models
# from datetime import datetime
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField


from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()



# store the messages in a database---------------------------------------------------------------- -
class BroadcastMessage(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:50]  # Display the first 50 characters in the admin interface

class PhoneNumber(models.Model):
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number
     
# therapist summary-------------------------------------------------------------------------------- 
class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/therapist')
    bio = models.CharField(max_length=250, default='', blank=True, null=True)

    def __str__(self):
        return self.bio[:50]
    