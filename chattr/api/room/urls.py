import rest_framework.urls

import api.room.views

app_name = 'room'

urlpatterns = [
    rest_framework.urls.path(
        'get_room/',
        api.homepage.views.NewRoom.as_view(),
        name='get_room',
    ),
]
