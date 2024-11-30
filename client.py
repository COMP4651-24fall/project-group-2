#client.py

import asyncio
import websockets

async def sendMessage():
    async with websockets.connect("ws://52.91.21.7:8765") as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.run(sendMessage())
