__all__ = []

import django.db.models

import core.models


class Message(django.db.models.Model):
    sender_id = django.db.models.CharField(
        verbose_name='ID of message sender'
    )
    sender_name = django.db.models.CharField(
        verbose_name='name of message sender'
    )
    ws_group = django.db.models.CharField(
        verbose_name='websocket group',
    )
    content = django.db.models.TextField(
        verbose_name='content',
    )
