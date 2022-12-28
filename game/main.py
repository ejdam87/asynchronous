import asyncio
import server as s
import client as c

async def main() -> None:

    port = 9052
    server = await s.open_server( port )
    await asyncio.gather( *[ c.connect(port) for _ in range(2) ] )

asyncio.run( main() )
