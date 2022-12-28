import asyncio

async def handle_client(reader, writer) -> None:
    
    data = await reader.read( 100 )
    message = data.decode()

    print( f"Received: {message}" )
    writer.write( data )
    await writer.drain()

    print( "Close the connection" )
    writer.close()


async def open_server( port: int ):
    print( f"Opening server at: {port}" )
    server = await asyncio.start_server( handle_client, host="127.0.0.1", port=port )
    return server

async def close_server( server ) -> None:
    print( "Closing server" )
    await server.close()
