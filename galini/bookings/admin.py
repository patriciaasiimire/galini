from django.contrib import admin
from .models import Appointment, Feedback, TimeSlot

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'requested_time', 'is_confirmed', 'confirmed_time')
    list_filter = ('is_confirmed', 'requested_time')
    search_fields = ('user__username', 'description')
    readonly_fields = ('requested_time', 'confirmed_time')
    fieldsets = (
        (None, {
            'fields': ('user', 'description')
        }),
        ('Confirmation', {
            'fields': ('is_confirmed', 'confirmed_time'),
            'classes': ('collapse',),
        }),
    )

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_time', 'end_time')
    list_filter = ('doctor', 'start_time')
    search_fields = ('doctor__username',)
    date_hierarchy = 'start_time'
    fieldsets = (
        (None, {
            'fields': ('doctor',)
        }),
        ('Time Slot Details', {
            'fields': ('start_time', 'end_time'),
        }),
    )


class FeedbackAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'created_at')  # Fields to display in the list view
  readonly_fields = ('created_at',)  # Make 'created_at' read-only

admin.site.register(Feedback, FeedbackAdmin)