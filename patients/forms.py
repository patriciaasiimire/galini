# patients/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Patient

class PatientProfileForm(UserChangeForm):
    class Meta:
        model = Patient
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'address', 'phone_number']
