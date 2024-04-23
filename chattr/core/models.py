__all__ = []

import django.contrib.auth.models
import django.db.models


class ChattrUser(django.contrib.auth.models.AbstractUser):
    identifier = django.db.models.CharField(
        name='identifier',
        verbose_name='UUID4 identifier',
        max_length=255,
        unique=True,
        db_index=True,
    )
    username = django.db.models.CharField(
        name='username',
        verbose_name='username',
        max_length=255,
    )


class Message(django.db.models.Model):
    sender = django.db.models.ForeignKey(
        ChattrUser,
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
