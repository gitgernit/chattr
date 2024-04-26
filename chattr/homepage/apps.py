__all__ = []

import django.apps


class HomepageConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'
    label = 'homepage'
    verbose_name = 'Homepage'
