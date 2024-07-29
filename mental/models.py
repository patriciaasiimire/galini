from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Chatroom----------------------------------------------------------------
class Room(models.Model):
    name = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True)

# store the meesages in a database---------------------------------------------------------------- -
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date_added',)
        

        
# therapist summary-------------------------------------------------------------------------------- 
class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/therapist')
    bio = models.CharField(max_length=250, default='', blank=True, null=True)

    def __str__(self):
        return self.name
    

# appointments were replaced with the chat