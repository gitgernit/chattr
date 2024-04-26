__all__ = []

import http
import uuid

import django.core.cache
import rest_framework.response
import rest_framework.views

import api.rooms.models
import api.rooms.serializers
import rooms.models

redis_client = django.core.cache.cache.client.get_client()


class CreateRoom(rest_framework.views.APIView):
    def post(self, request):
        serializer = api.rooms.serializers.RoomSettingsSerializer(
            data=request.query_params,
        )

        if serializer.is_valid():
            room_settings = serializer.validated_data
            room_id_parse = uuid.uuid4().hex

            new_room = api.rooms.models.Room(
                room_id=room_id_parse,
                max_users=room_settings['max_users'],
                max_idle_time=room_settings['max_idle_time'],
            )
            new_room.save()

            return rest_framework.response.Response(
                {
                    'room_id': room_id_parse,
                },  # Can later be changed to full link
            )

        return rest_framework.response.Response(
            serializer.errors,
            status=http.HTTPStatus.BAD_REQUEST,
        )


class GetMessages(rest_framework.views.APIView):
    def get(self, request):
        ws_group = request.query_params['ws_group']
        if not ws_group:
            return rest_framework.response.Response(
                {
                    'error': 'ws_group is required',
                },
                status=http.HTTPStatus.BAD_REQUEST,
            )

        messages = rooms.models.Message.objects.filter(
            ws_group=ws_group,
        )
        serializer = api.rooms.serializers.GetMessagesSerializer(
            messages,
            many=True,
        )
        return rest_framework.response.Response(serializer.data)
