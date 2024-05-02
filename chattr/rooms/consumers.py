__all__ = []

import json
import urllib.parse
import uuid

import asgiref.sync
import channels.generic.websocket
import django.contrib.sessions.models

import rooms.models


class RoomConsumer(channels.generic.websocket.AsyncWebsocketConsumer):
    async def connect(self):
        query_params = urllib.parse.parse_qs(self.scope['query_string'].decode())
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.username = query_params['username'][0]
        self.room_group_name = f'chat_{self.room_name}'

        if self.scope['session'].get('room') is not None:
            return

        self.scope['session']['room'] = self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, code):
        self.scope['user']['room'] = None

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        print(self.username)

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, 'username': self.username}
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event['username']

        await self.send(text_data=json.dumps({"message": message, 'username': username}))

    # async def send_sdp(self, event):
    #     if 'message' in event['data']:
    #         new_message = rooms.models.Message.objects.create(
    #             sender=self.scope['user'],
    #             content=event['data']['message'],
    #             ws_group=self.room_group_name,
    #         )
    #         await asgiref.sync.sync_to_async(new_message.save)()
    #
    #     await self.send(text_data=json.dumps(event['data']))
    #
    def get_session(self):
        session_key = self.scope['session'].session_key
        return django.contrib.sessions.models.Session.objects.get(
            session_key=session_key,
        )
