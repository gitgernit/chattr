import django.urls

import rooms.consumers

websocket_urlpatterns = [
    django.urls.re_path(
        r'ws/chat/(?P<room_name>\w+)/$',
        rooms.consumers.RoomConsumer.as_asgi(),
    ),
]
