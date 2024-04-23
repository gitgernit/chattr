from django.apps import AppConfig

__all__ = []


class ApiHomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.homepage'
    label = 'api_homepage'
    verbose_name = 'Создание комнаты'
