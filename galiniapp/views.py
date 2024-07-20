from django.shortcuts import render, get_object_or_404

from .models import Therapist

def home(request):
    return render(request, 'home.html', {})

def therapist_profile(request, id):
    therapist = Therapist.objects.all()
    return render(request, 'therapist_profile.html', {'therapist': therapist})