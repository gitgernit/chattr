__all__ = []

import rest_framework.serializers

import api.rooms.validators


class RoomSettingsSerializer(rest_framework.serializers.Serializer):
    max_users = rest_framework.serializers.IntegerField(
        default=24,
        validators=[api.rooms.validators.MaxUsersValidator(100)],
    )
    max_idle_time = rest_framework.serializers.IntegerField(
        default=1440,
        validators=[api.rooms.validators.MaxIdleTimeValidator(10080)],
    )
