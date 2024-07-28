from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Therapist, Room
from datetime import datetime
# from email.message import EmailMessage
# import logging
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# register
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, PHQ9Form
from .models import Message, Room
# from google.oauth2 import service_account
# from googleapiclient.discovery import build


def home(request):
    return render(request, 'home.html')

def therapists_summary(request):
    therapists = Therapist.objects.all()
    return render(request, 'therapists_summary.html', {'therapists': therapists})
# authentication----------------------------------------------------------------
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Ensure `request` is the first argument
            return redirect('home')  # Redirect to a home page or any other page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    # messages.success(request, ('You have been logged out, Thanks for stopping by...'))
    return redirect('home')

def register_user(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        form.save()
        new_user = authenticate(username=username, email=email, password=password)
        if new_user is not None:
            login(request, new_user)  # Ensure `request` is the first argument
            return redirect('home')  # Redirect to a home page or any other page
    form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

# PHQ9 FORM ----------------------------------------------------------------
def phq9_calculator_view(request):
    if request.method == 'POST':
        form = PHQ9Form(request.POST)
        if form.is_valid():
            score = form.calculate_score()
            return render(request, 'phq9_result.html', {'score': score})
    else:
        form = PHQ9Form()
    return render(request, 'phq9_calculator.html', {'form': form})

# Chat----------------------------------------------------------------
def message_page(request):
    return render(request,'message_page.html')

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]


    return render(request, 'room.html', {'room': room, 'messages':messages})