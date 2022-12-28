import asyncio

async def send_msg( port: int, msg: str ) -> None:

    reader, writer = await asyncio.open_connection(
        '127.0.0.1', port)

    print( f'Send: {msg}' )
    writer.write( msg.encode() )
    await writer.drain()

    data = await reader.read(100)
    print( f'Ack: {data.decode()!r}' )

    print( 'Close the connection' )
    writer.close()
