# disorders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.disorder_list, name='disorder_list'),
    path('<int:pk>/', views.disorder_detail, name='disorder_detail'),
]
