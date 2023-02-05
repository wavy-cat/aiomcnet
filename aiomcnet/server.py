import asyncio


class MinecraftServer:
    def __init__(self, host: str, port: int = 25565):
        self.host = host
        self.port = port

    async def ping(self, timeout=60, loop=None, read_bits: int = 2048):
        if timeout <= 0:
            # TODO: Add custom exception
            raise Exception('The timeout cannot be less than or equal to zero.')

        start = asyncio.get_running_loop().time()
        if loop:
            reader, writer = await asyncio.open_connection(self.host, self.port, loop=loop)
        else:
            reader, writer = await asyncio.open_connection(self.host, self.port)

        writer.write(b'\xfe\x01')
        await writer.drain()

        task = asyncio.create_task(reader.read(read_bits))
        done, pending = await asyncio.wait({task}, timeout=timeout)
        if task in done:
            data = task.result()
            writer.close()
        else:
            # TODO: Add custom exception
            writer.close()
            raise Exception('Timeout')

        end = asyncio.get_running_loop().time()

        if data[0] != 255:
            # TODO: Add custom exception
            raise Exception('Incorrect response')

        payload = data[3:].decode('utf-16be').split('\x00')

        return {
            'protocol_version': payload[1],
            'server_version': payload[2],
            'motd': payload[3],
            'players': {
                'current': payload[4],
                'max': payload[5]
            },
            'elapsed_time': end - start
        }
