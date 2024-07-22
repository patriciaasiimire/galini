from django.shortcuts import render, redirect

# Create your views here.
# therapists/views.py

#from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .models import Therapist

def therapist_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        therapist = Therapist.objects.create_user(username=username, password=password)
        login(request, therapist)
        return redirect('therapist_profile')
    return render(request, 'therapists/register.html')

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

@login_required(login_url='therapist_login')
def therapist_profile(request):
    user_form = UserChangeForm(instance=request.user)
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully.')
    return render(request, 'therapists/profile.html', {'user_form': user_form})
