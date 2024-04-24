__all__ = []

from django.apps import AppConfig


class ApiHomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.homepage'
    label = 'api_homepage'
    verbose_name = 'Используемое главной страницой'
