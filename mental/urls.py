from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('therapists_summary/', views.therapists_summary, name='therapists_summary'),

    path('embed/', views.embed_view, name='embed'),
    
    path('request_appointment/', views.request_appointment, name='request_appointment'),
    path('define_time_slots/', views.define_time_slots, name='define_time_slots'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),

    path('request_appointment/', views.request_appointment, name='request_appointment'),
]
