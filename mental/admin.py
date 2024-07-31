from django.contrib import admin
from .models import Therapist, Room, Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'value', 'date_added')

admin.site.register(Therapist)
admin.site.register(Room)
admin.site.register(Message)
