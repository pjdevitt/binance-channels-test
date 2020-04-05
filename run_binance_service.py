import os

from binance.client import Client
from binance.websockets import BinanceSocketManager
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

import asyncio

API_KEY = ""
API_SECRET_KEY = ""


loop = asyncio.get_event_loop()
    
def process_message(message):
    print(message)
    channel_layer = get_channel_layer()
    try:
        async_to_sync(channel_layer.group_send)("stockdata", {"type": "recv.stockdata", "message": message})
    except:
        print("execption!")
    

async def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channeltest.settings')
    client = Client(API_KEY, API_SECRET_KEY)
    bm = BinanceSocketManager(client)
    bm.start_trade_socket('BNBBTC', process_message)
    bm.start()
    
loop.run_until_complete(main())
loop.close()