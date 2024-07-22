from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

from patients.forms import PatientProfileForm
from .models import Patient

def patient_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        patient = Patient.objects.create_user(username=username, password=password)
        login(request, patient)
        return redirect('patient_profile')
    return render(request, 'patients/register.html')

def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('patient_profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'patients/login.html')

@login_required
def patient_logout(request):
    logout(request)
    return redirect('patient_login')

@login_required
def patient_profile(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('patient_profile')
    else:
        form = PatientProfileForm(instance=request.user)
    return render(request, 'patients/profile.html', {'form': form})


