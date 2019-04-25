from channels.generic.websocket import AsyncWebsocketConsumer
import json


class PaymentConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = 'PAYMENT_CHANNEL_GROUP'

    async def connect(self):
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)

    async def payment_message(self, event):
        message = event['message']
        print('payment message: %s' % message)
        # Send message to WebSocket
        await self.send(text_data=message)