__all__ = []

import django.contrib.admin
import django.urls

import api.urls
import homepage.urls

urlpatterns = [
    django.urls.path(
        '',
        django.urls.include(homepage.urls),
    ),
    django.urls.path(
        'api/',
        django.urls.include(api.urls),
    ),
    django.urls.path(
        'admin/',
        django.contrib.admin.site.urls,
    ),
]
