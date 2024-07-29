from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/<str:room_name>/$', consumers.MentalConsumer.as_asgi()),
]