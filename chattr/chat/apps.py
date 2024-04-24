__all__ = []

from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
    label = 'chat'
    verbose_name = 'Websocket-chat'
