__all__ = []

import django.apps


class RoomsConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rooms'
    label = 'rooms'
    verbose_name = 'Chat rooms'
