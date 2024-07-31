from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Therapist, Room, Message

from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# register
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, PHQ9Form
from .models import Message, Room


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

# PHQ9 FORM --------------------------------------------------------------------------------
def phq9_calculator_view(request):
    if request.method == 'POST':
        form = PHQ9Form(request.POST)
        if form.is_valid():
            score = form.calculate_score()
            return render(request, 'phq9_result.html', {'score': score})
    else:
        form = PHQ9Form()
    return render(request, 'phq9_calculator.html', {'form': form})

# video chat--------------------------------------------------------------------------------
@login_required
def dashboard_chat(request):
    return render(request, 'dashboard_chat.html')

# old version Chat----------------------------------------------------------------
# def message_page(request):
#     return render(request,'message_page.html')

# @login_required
# def room(request, room):
#     username = request.GET.get('username')
#     room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'room_details': room_details,
#         'username': username,
#         'room': room
#     })

# @login_required
# def checkview(request):
#     room = request.POST['room_name']
#     username = request.POST['username']
    
#     if Room.objects.filter(name=room).exists():
#         return redirect('/'+room+'/?username='+username)
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('/'+room+'/?username='+username)

# @login_required
# def send(request):
#     message = request.POST['message']
#     username = request.POST['username']
#     room_id = request.POST['room_id']

#     new_message = Message.objects.create(value=message, username=username, room=room_id)
#     new_message.save()
#     return HttpResponse('Message sent successfully')
    
# @login_required
# def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages': list(messages.values())})