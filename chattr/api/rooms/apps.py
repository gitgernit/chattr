__all__ = []

import django.apps


class ApiHomepageConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.rooms'
    label = 'api_rooms'
    verbose_name = 'Room-control'
