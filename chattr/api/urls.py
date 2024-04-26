__all__ = []

import django.urls
import rest_framework.urls

import api.rooms.urls

app_name = 'api'

urlpatterns = [
    rest_framework.urls.path(
        'rooms/',
        django.urls.include(api.rooms.urls),
    ),
]
