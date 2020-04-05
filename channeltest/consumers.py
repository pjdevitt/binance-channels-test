from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
import json
import datetime

class WebClientConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("stockdata", self.channel_name)
        
    async def disconnect(self, close_code):
        pass
        
    async def recv_stockdata(self, event):
        await self.send_json(event['message'])
