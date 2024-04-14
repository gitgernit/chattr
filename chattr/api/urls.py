__all__ = []

import django.urls
import rest_framework.urls

import api.homepage.urls

app_name = 'api_homepage'

urlpatterns = [
    rest_framework.urls.path(
        'homepage/',
        django.urls.include(api.homepage.urls),
        name='get_room',
    ),
]
