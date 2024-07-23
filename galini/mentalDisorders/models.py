# disorders/models.py
from django.db import models

class MentalDisorder(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    causes = models.TextField()

    def __str__(self):
        return self.name
