from django.contrib import admin
from .models import Therapist, Room, Message

admin.site.register(Therapist)
admin.site.register(Room)
admin.site.register(Message)
