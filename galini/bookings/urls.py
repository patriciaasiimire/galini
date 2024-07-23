from django.urls import path
from django.conf.urls.static import static
from galini import settings
from . import views

urlpatterns = [
    path('request_appointment/', views.request_appointment, name='request_appointment'),
    path('define_time_slots/', views.define_time_slots, name='define_time_slots'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),  # Add this line
    # Add more URLs as needed
]

