from django.shortcuts import render, redirect
from .models import TherapistProfile

def home(request):
    return render(request, 'home.html')

def therapist_profile(request):
    return render(request, 'therapist_profile.html', {})

def therapist(request, pk):
    therapist = TherapistProfile.objects.all(id=pk)
    return render(request, 'therapist.html', {'therapist': therapist})
