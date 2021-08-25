import asyncio
import random
import websockets

async def message(websocket, path):
    while True:
        await websocket.send(str(int(random.random() * 20)))
        await asyncio.sleep(3)

start_server = websockets.serve(message,'localhost',1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()