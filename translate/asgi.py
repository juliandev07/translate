"""
ASGI config for translate project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'translate.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # URL to HTTP.
    "websocket": AuthMiddlewareStack(  # URL to websockets.
            URLRouter(
                routing.websocket_urlpatterns
            )
        ),

})
