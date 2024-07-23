# bookings/forms.py

from django import forms
from .models import Appointment, Feedback, TimeSlot

class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, you can add more customization here
        self.fields['start_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select start time'})
        self.fields['end_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select end time'})



class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user', 'description']  # Adjust fields based on your Appointment model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter description'})
        # Add more fields as necessary and customize their attributes

from django import forms

class FeedbackForm(forms.Form):
  name = forms.CharField(max_length=255, required=False)  # Optional name field
  email = forms.EmailField(required=True)
  message = forms.CharField(widget=forms.Textarea, required=True)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your name (optional)'})
    self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
    self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write your feedback here'})
