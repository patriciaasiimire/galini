from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('therapists/', include('therapists.urls')),
    path('', home_view, name='home'),

    # Serve a homepage or a view for the root URL
]
