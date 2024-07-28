from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
    path('therapists_summary/', views.therapists_summary, name='therapists_summary'),

    path('message_page/', views.message_page, name='message_page'),
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),

    path('phq9/calculator/', views.phq9_calculator_view, name='phq9_calculator'),
    
]
