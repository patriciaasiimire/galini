# patients/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.patient_register, name='patient_register'),
    path('login/', views.patient_login, name='patient_login'),
    path('logout/', views.patient_logout, name='patient_logout'),
    path('profile/', views.patient_profile, name='patient_profile'),
]
