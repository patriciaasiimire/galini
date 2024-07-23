# bookings/views.py

from datetime import datetime
from email.message import EmailMessage
import logging
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from bookings.forms import AppointmentRequestForm, FeedbackForm, TimeSlotForm
from .models import Appointment
from google.oauth2 import service_account
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

@login_required
def request_appointment(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        appointment = Appointment.objects.create(user=request.user, description=description)
        # Send email notification to user or other actions
        return render(request, 'appointment_requested.html', {'appointment': appointment})
    return render(request, 'bookings/request_appointment.html')


@login_required
def define_time_slots(request):
    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            time_slot = form.save(commit=False)
            time_slot.doctor = request.user  # Assign the current user as the doctor
            time_slot.save()
            return redirect('define_time_slots')  # Replace with your URL name for listing time slots
    else:
        form = TimeSlotForm()
    
    context = {
        'form': form,
    }
    return render(request, 'bookings/define_time_slots.html', context)


def send_appointment_notification(appointment):
    subject = 'Appointment Requested'
    message = f'Your appointment has been requested. Description: {appointment.description}'
    from_email = 'your_email@example.com'
    recipient_list = [appointment.user.email]
    send_mail(subject, message, from_email, recipient_list) # type: ignore


def add_to_google_calendar(appointment):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = 'path/to/service-account-file.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)

    event = {
      'summary': f'Appointment with {appointment.user.username}',
      'description': appointment.description,
      'start': {
        'dateTime': appointment.requested_time.strftime('%Y-%m-%dT%H:%M:%S'),
        'timeZone': 'Your/Timezone',
      },
      'end': {
        'dateTime': (appointment.requested_time + datetime.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%S'),
        'timeZone': 'Your/Timezone',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


@login_required
def request_appointment(request):
    if request.method == 'POST':
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or process it further
            appointment = form.save(commit=False)
            appointment.user = request.user  # Assuming appointment has a 'user' field for the requesting user
            appointment.save()
            return redirect('appointment_requested')
    else:
        form = AppointmentRequestForm()

    return render(request, 'bookings/request_appointment.html', {'form': form})

@login_required
def appointment_requested(request):
    return render(request, 'bookings/appointment_requested.html')

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new Appointment object
            appointment = form.save(commit=False)
            appointment.user = request.user  # Assuming request.user is authenticated and assigned
            appointment.save()
            return redirect('appointment_detail', pk=appointment.pk)  # Redirect to appointment detail page
    else:
        form = AppointmentRequestForm()
    return render(request, 'bookings/appointment_form.html', {'form': form})

def submit_feedback(request):
  if request.method == 'POST':
    form = FeedbackForm(request.POST)
    if form.is_valid():
      feedback = form.save()  # Save feedback data to database
      send_feedback_notification(feedback.email)  # Call notification function with email
      return redirect('appointment_confirmation')  # Redirect to confirmation page
  else:
    form = FeedbackForm()
  return render(request, 'bookings/feedback_form.html', {'form': form})

def send_feedback_notification(email_address):
  # Your email server details (replace with your actual details)
  sender_email = "your_email@example.com"
  subject = "New Feedback Received"
  message = f"""
  A new feedback has been submitted from {email_address}.

  Please check your dashboard for details.

  This is an automated notification from your appointment system.
  """

  try:
    email = EmailMessage(subject, message, sender_email, [email_address])
    email.send()
  except Exception as e:
    print(f"Error sending email notification: {e}")

