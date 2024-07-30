import django.urls

import rooms.consumers

websocket_urlpatterns = [
    django.urls.re_path(r"ws/rooms/(?P<room_id>\w+)$",
                        rooms.consumers.RoomConsumer.as_asgi(),
                        )
]
