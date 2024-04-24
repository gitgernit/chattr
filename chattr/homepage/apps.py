from django.apps import AppConfig

__all__ = []


class HomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'
    label = 'homepage'
    verbose_name = 'Главная страница'
