__all__ = []

import django.db.models

import core.models


class Message(django.db.models.Model):
    sender = django.db.models.ForeignKey(
        core.models.ChattrUser,
        name='sender',
        on_delete=django.db.models.CASCADE,
        related_name='sent_messages',
    )
    ws_group = django.db.models.CharField(
        name='ws_group',
        verbose_name='websocket group',
    )
    content = django.db.models.TextField(
        name='content',
        verbose_name='content',
    )
