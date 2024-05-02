__all__ = []

import django.urls
import django.views.generic

import rooms.views

app_name = 'rooms'

urlpatterns = [
    django.urls.path(
        '<str:room_id>/',
        rooms.views.RoomView.as_view(),
        name='room',
    ),
]
