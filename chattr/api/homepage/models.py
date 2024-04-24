__all__ = []

import django.db.models

import api.homepage.validators


class Room(django.db.models.Model):
    room_id = django.db.models.CharField(
        'ID',
        db_index=True,
    )
    max_users = django.db.models.IntegerField(
        'MaxUsers',
        validators=[
            api.homepage.validators.MaxUsersValidator(100),
        ],
        default=24,
    )
    max_time = django.db.models.IntegerField(
        'MaxTime',
        validators=[
            api.homepage.validators.MaxIdleTimeValidator(10080),
        ],
        default=1440,
    )
