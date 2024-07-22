from django.urls import path
from . import views

urlpatterns = [
    # Mental Health Home Page
    path('', views.home, name='home'),
    path('therapist_profile/', views.therapist_profile, name='therapist_profile'),
]

