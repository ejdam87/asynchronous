import asyncio

async def send_msg( port: int, msg: str ) -> None:

    print( f"Sending: {msg}" )
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    writer.write( msg.encode() )
