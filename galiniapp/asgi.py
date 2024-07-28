import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

# Channels configuration for Mental app
import mental.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galiniapp.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            mental.routing.websocket_urlpatterns
        )
    ),
})
