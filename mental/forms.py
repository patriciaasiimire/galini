
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Therapist, Appointment, Feedback, TimeSlot

# therapists
class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['name', 'specialty', 'email', 'phone']

class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, you can add more customization here
        self.fields['start_time'].widget.attrs.update({ 'placeholder': 'Select start time'})
        self.fields['end_time'].widget.attrs.update({ 'placeholder': 'Select end time'})


# appointments
class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user', 'description']  # Adjust fields based on your Appointment model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({ 'placeholder': 'Enter description'})
        # Add more fields as necessary and customize their attributes



class FeedbackForm(forms.Form):
  name = forms.CharField(max_length=255, required=False)  # Optional name field
  email = forms.EmailField(required=True)
  message = forms.CharField(widget=forms.Textarea, required=True)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['name'].widget.attrs.update({ 'placeholder': 'Enter your name (optional)'})
    self.fields['email'].widget.attrs.update({ 'placeholder': 'Enter your email'})
    self.fields['message'].widget.attrs.update({ 'placeholder': 'Write your feedback here'})

# registration forms
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
              'required':'',
              'name':'username',
              'type':'text',
              'class':'input-box',
              'placeholder':'Username'
          })

        self.fields['email'].widget.attrs.update({
              'required': '',
              'name':"email",
              'type':"email",
              'class':'input-box',
              'placeholder':"email address"
          })

        self.fields['password1'].widget.attrs.update({
              'required': '',
              'name':"password1",
              'type':"password",
              'class':'input-box',
              'placeholder':"password"
          })
        self.fields['password2'].widget.attrs.update({
              'required': '',
              'name':"password2",
              'type':"password",
              'class':'input-box',
              'placeholder':"confirm password"
          })
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')