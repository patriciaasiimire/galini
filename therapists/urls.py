# therapists/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.therapist_register, name='therapist_register'),
    path('login/', views.therapist_login, name='therapist_login'),
    path('logout/', views.therapist_logout, name='therapist_logout'),
    path('profile/', views.therapist_profile, name='therapist_profile'),
]
