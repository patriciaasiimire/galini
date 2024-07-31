from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),


    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    

    path('therapists_summary/', views.therapists_summary, name='therapists_summary'),

    path('dashboard_chat/', views.dashboard_chat, name='dashboard_chat'),
    path('meeting/', views.videocall, name='meeting'),
    path('join/', views.join, name='join'),
    
    # path('<str:room>/', views.room, name='room'),
    # path('message_page', views.message_page, name='message_page'),
    # path('checkview', views.checkview, name='checkview'),
    # path('send', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    

    path('phq9/calculator/', views.phq9_calculator_view, name='phq9_calculator'),
    
]
