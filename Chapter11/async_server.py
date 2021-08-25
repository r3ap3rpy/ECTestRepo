import asyncio
from asyncio.streams import start_server
import websockets

async def response(websocket, path):
    message = await websocket.recv()
    print(f"We got the following message from the client: {message}")
    await websocket.send(f"I got your message <{message}>")

start_server = websockets.serve(response,'localhost',1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()