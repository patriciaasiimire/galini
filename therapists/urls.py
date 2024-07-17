from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('<int:pk>/', views.therapist_detail, name='therapist_detail'),
]
