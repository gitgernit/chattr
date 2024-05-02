__all__ = []

import django.contrib.admin
import django.urls
import django.views.generic

import api.urls
import homepage.urls
import rooms.urls

urlpatterns = [
    django.urls.path(
        '',
        django.urls.include(homepage.urls),
    ),
    django.urls.path(
        'rooms/',
        django.urls.include(rooms.urls),
    ),
    django.urls.path(
        'webrtc/',
        django.views.generic.TemplateView.as_view(template_name='index.html'),
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
