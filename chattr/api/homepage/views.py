__all__ = []

import uuid

import django.core.cache
import rest_framework.response
import rest_framework.views

import api.homepage.serializers

redis_client = django.core.cache.cache.client.get_client()


class NewRoom(rest_framework.views.APIView):
    def get(self, request):
        serializer = api.homepage.serializers.RoomSettingsSerializer(
            data=request.query_params,
        )

        if serializer.is_valid():
            room_settings = serializer.validated_data
            room_id = uuid.uuid4().hex

            redis_client.hset(room_id, mapping=room_settings)

            return rest_framework.response.Response(
                {'room_id': room_id},  # Can later be changed to full link
            )

        return rest_framework.response.Response(serializer.errors, status=400)
