from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm  # Import the form

def therapist_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_therapist = True
            user.save()
            login(request, user)
            return redirect('therapist_profile')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'therapists/register.html', {'form': form})

def therapist_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('therapist_profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'therapists/login.html')

@login_required
def therapist_logout(request):
    logout(request)
    return redirect('therapist_login')

@login_required
def therapist_profile(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('therapist_profile')
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, 'therapists/profile.html', {'form': form})
