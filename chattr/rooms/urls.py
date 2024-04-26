__all__ = []

import django.urls
import django.views.generic

app_name = 'rooms'

urlpatterns = [
    django.urls.path(
        '<room_id:uuid>/',
        django.views.generic.TemplateView.as_view(template_name='index.html'),
        name='room',
    ),
]
