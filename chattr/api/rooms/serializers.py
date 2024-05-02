__all__ = []

import django.db.models.fields
import rest_framework.serializers

import api.rooms.models
import rooms.models


class ModelSerializerDefaultsMixin:
    def __init__(self, *args, **kwargs):
        extra_kwargs = {}

        for field in self.Meta.model._meta.fields:
            if field.default != django.db.models.fields.NOT_PROVIDED:
                extra_kwargs[field.name] = {'default': field.default}

        self.Meta.extra_kwargs = extra_kwargs
        super(ModelSerializerDefaultsMixin, self).__init__(*args, **kwargs)


class RoomSettingsSerializer(
    ModelSerializerDefaultsMixin,
    rest_framework.serializers.ModelSerializer,
):
    class Meta:
        model = api.rooms.models.Room
        fields = ('max_users', 'max_idle_time')


class GetMessagesSerializer(
    ModelSerializerDefaultsMixin,
    rest_framework.serializers.ModelSerializer,
):
    class Meta:
        model = rooms.models.Message
        fields = ('sender', 'ws_group', 'content')
