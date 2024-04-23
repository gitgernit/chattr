import django.db.models

class Rooms(django.db.models.Model):
    room_id = django.db.models.CharField(
        'ID',
        db_index=True,
    )
    max_users = django.db.models.IntegerField(
        'MaxUsers',
        max_length=100,
        default=24,
    )
    max_time = django.db.models.IntegerField(
        'MaxTime',
        max_length=10080,
        default=1440,
    )
