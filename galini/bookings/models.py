# bookings/models.py

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
