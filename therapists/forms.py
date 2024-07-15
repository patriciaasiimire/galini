from django import forms
from django.contrib.auth.models import User
from .models import Therapist

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['specialization', 'contact_number', 'email', 'address', 'bio']