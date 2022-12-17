import asyncio

async def handle_client(reader, writer) -> None:
    
    print( "Handling client" )
    data = await reader.read()
    msg = data.decode()
    print(f" Message: {msg}")


async def open_server( port: int ):
    print(f"Opening server at: {port}")
    server = await asyncio.start_server(handle_client, host="127.0.0.1", port=port)
    return server

async def close_server( server ) -> None:
    print("Closing server")
    await server.close()
