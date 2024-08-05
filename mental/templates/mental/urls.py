from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('translate/', views.translate_view, name='translate'),

    path('broadcast/', views.broadcast_sms, name='broadcast'),


    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
    path('phq9_calculator/', views.fetch_phq9_calculator, name='fetch_phq9_calculator'),

    path('therapists_summary/', views.therapists_summary, name='therapists_summary'),

    path('dashboard_chat/', views.dashboard_chat, name='dashboard_chat'),
    path('meeting/', views.videocall, name='meeting'),
    path('join/', views.join, name='join'),

    path('appointment/', views.appointment, name='appointment'),
    

    path('phq9/calculator/', views.phq9_calculator_view, name='phq9_calculator'),
    
]
