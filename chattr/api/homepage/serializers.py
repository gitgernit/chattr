__all__ = []

import rest_framework.serializers

import api.homepage.validators


class RoomSettingsSerializer(rest_framework.serializers.Serializer):
    max_users = rest_framework.serializers.IntegerField(
        default=24,
        validators=[api.homepage.validators.MaxUsersValidator(100)],
    )
    max_idle_time = rest_framework.serializers.IntegerField(
        default=1440,
        validators=[api.homepage.validators.MaxIdleTimeValidator(10080)],
    )
