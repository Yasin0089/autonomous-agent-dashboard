import asyncio
import websockets

clients = set()

async def notify_clients(message):
    if clients:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([client.send(message) for client in clients])

async def register(client):
    clients.add(client)
    try:
        await client.wait_closed()
    finally:
        clients.remove(client)

async def handler(websocket, path):
    await register(websocket)
    while True:
        try:
            message = await websocket.recv()
            await notify_clients(message)
        except websockets.ConnectionClosed:
            break

if __name__ == '__main__':
    start_server = websockets.serve(handler, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    print('WebSocket server started on ws://localhost:8765')
    asyncio.get_event_loop().run_forever()