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
        db_index=True,
    )
    room_name = django.db.models.CharField(
        name='room_name',
        verbose_name='room name',
        max_length=255,
        unique=True,
    )
    send_time = django.db.models.DateTimeField(
        name='send_time',
        verbose_name='send time',
        auto_now_add=True,
    )
