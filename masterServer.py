#masterServer.py

import asyncio
import websockets

async def master_handler(websocket):
    async for message in websocket:
        print(f"Received from client: {message}")
        # Forward the message to the slave instance and get a response
        slave_response = await communicate_with_slave(message)
        await websocket.send(f"Response from slave: {slave_response}")

async def communicate_with_slave(message):
    slave_uri = "ws://172.31.94.234:8766"  # Replace <SLAVE_PRIVATE_IP> with th>
    async with websockets.connect(slave_uri) as slave_websocket:
        await slave_websocket.send(message)
        response = await slave_websocket.recv()
        return response

async def main():
    async with websockets.serve(master_handler, "0.0.0.0", 8765):  # Master lis>
        print("Master WebSocket server running on port 8765...")
        await asyncio.Future()  # Keep the server running forever

asyncio.run(main())

