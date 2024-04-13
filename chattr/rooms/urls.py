import rest_framework.urls

import rooms.views

app_name = 'rooms'

urlpatterns = [
    rest_framework.urls.path(
        'get_room/',
        rooms.views.NewRoom.as_view(),
        name='get_room',
    ),
]
