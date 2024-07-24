from django.db import models
import datetime

# class Patient(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=250, default='')
#     image = models.ImageField(upload_to='uploads/patient')

#     def __str__(self):
#         return self.name

class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/therapist')
    bio = models.CharField(max_length=250, default='', blank=True, null=True)

    def __str__(self):
        return self.name
    
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    requested_time = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    confirmed_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Appointment for {self.user.username} at {self.requested_time}"


class TimeSlot(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Time slot for {self.doctor.username} from {self.start_time} to {self.end_time}"
    
    
class Feedback(models.Model):
  name = models.CharField(max_length=255, blank=True)  # Optional name field
  email = models.EmailField()
  message = models.TextField()
  # Additional feedback fields if needed (e.g., rating, appointment ID)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name} - {self.email}"  # Customize string representation for clarity