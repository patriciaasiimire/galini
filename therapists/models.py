from django.db import models
from django.contrib.auth.models import User

class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reviewer} - {self.therapist.name}'
