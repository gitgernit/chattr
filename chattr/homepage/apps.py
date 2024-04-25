__all__ = []

from django.apps import AppConfig


class HomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'
    label = 'rooms'
    verbose_name = 'Homepage'
