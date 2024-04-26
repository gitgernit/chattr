__all__ = []

import os

import channels.auth
import channels.routing
import channels.security.websocket
import django.core.asgi

import rooms.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chattr.settings')

django_asgi_app = django.core.asgi.get_asgi_application()

application = channels.routing.ProtocolTypeRouter(
    {
        'http': django_asgi_app,
        'websocket': channels.security.websocket.AllowedHostsOriginValidator(
            channels.auth.AuthMiddlewareStack(
                channels.routing.URLRouter(
                    rooms.routing.websocket_urlpatterns,
                ),
            ),
        ),
    },
)
