import asyncio
import server as s
import client as c

async def main() -> None:

    port = 8842
    server = await s.open_server( port )
    async with server:
        await server.serve_forever()

asyncio.run( main() )
