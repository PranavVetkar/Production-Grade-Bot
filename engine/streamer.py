import websockets
import json

async def get_live_stream(symbol="btcusdt"):
    url = f"wss://stream.binance.com:9443/ws/{symbol}@ticker"
    async with websockets.connect(url) as websocket:
        while True:
            msg = await websocket.recv()
            yield json.loads(msg)