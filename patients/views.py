from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, PatientProfile

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

def patient_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            login(request, user)
            return redirect('patient_profile')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'patients/register.html', {'form': form})

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
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('patient_profile')
    else:
        form = UserCreationForm(instance=request.user)
    return render(request, 'patients/profile.html', {'form': form})

# Similar views for therapist
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
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('therapist_profile')
    else:
        form = UserCreationForm(instance=request.user)
    return render(request, 'therapists/profile.html', {'form': form})
