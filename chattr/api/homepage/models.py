__all__ = []

import django.db.models

import api.homepage.validators


class Room(django.db.models.Model):
    room_id = django.db.models.CharField(
        verbose_name='идентификатор комнаты',
        db_index=True,
    )
    max_users = django.db.models.IntegerField(
        verbose_name='максимальное количество пользователей',
        validators=[
            api.homepage.validators.MaxUsersValidator(100),
        ],
        default=24,
    )
    max_idle_time = django.db.models.IntegerField(
        verbose_name='максимальное время бездействия комнаты',
        validators=[
            api.homepage.validators.MaxIdleTimeValidator(10080),
        ],
        default=1440,
    )
