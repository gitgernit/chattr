__all__ = []

import django.urls
import rest_framework.urls

import api.room.urls

app_name = 'api'

urlpatterns = [
    rest_framework.urls.path(
        'room/',
        django.urls.include(api.homepage.urls),
    ),
]
