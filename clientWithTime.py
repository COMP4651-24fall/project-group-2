import asyncio
import websockets
import time

async def sendMessage():
    start_time = time.time() # Record the start time

    async with websockets.connect("ws://44.203.116.40:8765") as websocket:
        await websocket.send("Hello, Server!") # Send the message to the master server to establish communication
        
        response = await websocket.recv() # Wait for the response from the master server (originating from the slave server)
        
        end_time = time.time() # Record the end time
        
        # Calculate and print the time taken
        print(f"Response from server: {response}")
        print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(sendMessage())
