__all__ = []

from django.apps import AppConfig


class ApiHomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.rooms'
    label = 'api_rooms'
    verbose_name = 'Room-control'
