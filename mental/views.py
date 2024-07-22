from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def therapist_profile(request):
    return render(request, 'therapist_profile.html')