__all__ = []

import rest_framework.urls

import api.rooms.views

app_name = 'api-rooms'

urlpatterns = [
    rest_framework.urls.path(
        'get_room/',
        api.rooms.views.GetRoom.as_view(),
        name='get-room',
    ),
]
