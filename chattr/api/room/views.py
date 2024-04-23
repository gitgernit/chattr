__all__ = []

import uuid

import django.core.cache
import rest_framework.response
import rest_framework.views

import api.room.serializers
import api.room.models

redis_client = django.core.cache.cache.client.get_client()


class NewRoom(rest_framework.views.APIView):
    def get(self, request):
        serializer = api.homepage.serializers.RoomSettingsSerializer(
            data=request.query_params,
        )

        if serializer.is_valid():
            room_settings = serializer.validated_data
            room_id_parse = uuid.uuid4().hex

            new_room = api.homepage.models.Rooms(
                room_id = room_id_parse,
                max_users = room_settings['max_users'],
                max_time = room_settings['max_idle_time']
            )
            new_room.save()

            # redis_client.hset(room_id_parse, mapping=room_settings)

            return rest_framework.response.Response(
                {'room_id': room_id_parse},  # Can later be changed to full link
            )

        return rest_framework.response.Response(serializer.errors, status=400)
