import rest_framework.serializers

import rooms.validators


class RoomSettingsSerializer(rest_framework.serializers.Serializer):
    max_users = rest_framework.serializers.IntegerField(
        default=24, validators=[rooms.validators.MaxUsersValidator(100)]
    )
    max_idle_time = rest_framework.serializers.IntegerField(
        default=1440, validators=[rooms.validators.MaxIdleTimeValidator(10080)]
    )
