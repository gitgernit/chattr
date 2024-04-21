import rest_framework.urls

import api.homepage.views

app_name = 'homepage'

urlpatterns = [
    rest_framework.urls.path(
        'get_room/',
        api.homepage.views.NewRoom.as_view(),
        name='get_room',
    ),
]
