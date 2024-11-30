#slaveServer.py

import asyncio
import websockets

async def slave_handler(websocket):
    async for message in websocket:
        print(f"Received from master: {message}")
        await websocket.send(f"Slave response: {message[::-1]}")  # Send revers>

async def main():
    async with websockets.serve(slave_handler, "0.0.0.0", 8766):  # Listen on a>
        print("Slave WebSocket server running on port 8766...")
        await asyncio.Future()  # Keep the server running forever

asyncio.run(main())