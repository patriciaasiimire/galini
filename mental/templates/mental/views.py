from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Therapist, BroadcastMessage
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, AppointmentForm
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.utils.translation import activate, get_language, gettext
from .translation_utils import translate_text
from bs4 import BeautifulSoup
import requests


# views.py
def fetch_phq9_calculator(request):
    url = "https://www.mdcalc.com/calc/1725/phq9-patient-health-questionnaire9"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        return render(request, 'phq9_calculator.html', {'content': content})
    else:
        return HttpResponse("Failed to retrieve content", status=500)

def translate_view(request):
    text = request.GET.get('text', '')
    target_language = request.GET.get('target_language', 'en')
    translated_text = translate_text(text, target_language)
    return JsonResponse({'translated_text': translated_text})

def translate(language):
    curl_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(curl_language)
    return text
def broadcast_sms(request):
    try:
        # Fetch the latest message content from the database
        message_to_broadcast = BroadcastMessage.objects.latest('id').content
    except BroadcastMessage.DoesNotExist:
        return HttpResponse("No message to broadcast.", status=404)

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    # Iterate through the list of recipients
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        print(recipient)
        if recipient:
            # Ensure recipient is in E.164 format
            if not recipient.startswith('+'):
                recipient = f'+{recipient}'
            try:
                # Send the SMS message
                client.messages.create(
                    to=recipient,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    body=message_to_broadcast
                )
            except TwilioRestException as e:
                # Log any errors during the message sending
                print(f"Failed to send message to {recipient}: {str(e)}")
    
    return HttpResponse(f"Messages sent: {message_to_broadcast}", status=200)
                                   
def home(request):
    trans = translate(language=request.POST.get('language'))
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
    return render(request, 'phq9_calculator.html')

# video chat--------------------------------------------------------------------------------
@login_required
def dashboard_chat(request):
    user = request.user
    name = f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else user.username
    return render(request, 'dashboard_chat.html', {'name': name})

@login_required
def videocall(request):
    user = request.user
    name = f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else user.username
    return render(request, 'mental/meeting.html', {'name': name})

@login_required
def join(request):
    if request.method == 'POST':
       roomID = request.POST['roomID']
       return redirect('/meeting?roomID='+ roomID)
    return render(request, 'mental/join.html')
# appointment
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Process the data, for example, send an email or save to the database
            yourname = form.cleaned_data['yourname']
            # You can handle the form data here, such as sending an email or saving to a database
            return render(request, 'appointment.html', {'yourname': yourname})
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form})
