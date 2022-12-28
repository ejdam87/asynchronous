import asyncio

clients = {}

Server = asyncio.base_events.Server

async def handle_client(reader: asyncio.StreamReader,
                        writer: asyncio.StreamWriter) -> None:

    binary = await reader.read( 100 )
    move = binary.decode()

    addr = writer.get_extra_info('peername')
    clients[ addr ] = ( reader, writer )

    print( f"Received: {move}" )
    while len( clients ) != 2:
        writer.write( "Waiting".encode() )
        await writer.drain()
        binary = await reader.read( 100 )

    writer.write( "done".encode() )
    await writer.drain()
    print( "Close the connection" )
    writer.close()


async def open_server( port: int ) -> Server:
    print( f"Opening server at: {port}" )
    server = await asyncio.start_server( handle_client, host="127.0.0.1", port=port )
    return server

async def close_server( server: Server ) -> None:
    print( "Closing server" )
    await server.close()
