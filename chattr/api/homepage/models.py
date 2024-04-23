__all__ = []

import django.db.models


class Room(django.db.models.Model):
    room_id = django.db.models.CharField(
        'ID',
        db_index=True,
    )
    max_users = django.db.models.IntegerField(
        'MaxUsers',
        default=24,
    )
    max_time = django.db.models.IntegerField(
        'MaxTime',
        default=1440,
    )
