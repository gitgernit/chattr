__all__ = []

from django.urls import path
import django.views.generic

app_name = 'homepage'

urlpatterns = [
    path(
        '',
        django.views.generic.TemplateView.as_view(template_name='index.html'),
        name='homepage',
    ),
]
