import asyncio

async def connect( port: int ) -> None:

    reader, writer = await asyncio.open_connection('127.0.0.1', port)

    ack = ""
    while ack != "done":
        print( f'Sending' )
        writer.write( "Hi".encode() )
        await writer.drain()

        data = await reader.read(100)
        ack = data.decode()
        print( f'Ack: {ack}' )

    print( 'Close the connection' )
    writer.close()
