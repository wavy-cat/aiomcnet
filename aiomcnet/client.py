import asyncio
from aiomcnet.formatting_types import NoneFormat, TerminalFormat


class Client:
    def __init__(self, timeout: int = 60, loop: asyncio.AbstractEventLoop | None = None,
                 formatting: NoneFormat = TerminalFormat):
        if timeout <= 0:
            # TODO: Add custom exception
            raise Exception('The timeout cannot be less than or equal to zero.')

        self.timeout = timeout
        self.loop = loop
        self.formatting = formatting

    async def ping(self, host: str, port: int = 25565, read_bits: int = 2048):
        start = asyncio.get_running_loop().time()
        if self.loop:
            reader, writer = await asyncio.open_connection(host, port, loop=self.loop)
        else:
            reader, writer = await asyncio.open_connection(host, port)

        writer.write(b'\xfe\x01')
        await writer.drain()

        task = asyncio.create_task(reader.read(read_bits))
        done, pending = await asyncio.wait({task}, timeout=self.timeout)
        if task in done:
            data = task.result()
            writer.close()
        else:
            # TODO: Add custom exception
            writer.close()
            raise TimeoutError('Timeout')

        end = asyncio.get_running_loop().time()

        if data == b'':
            # TODO: Add custom exception
            raise Exception('The server did not respond')
        elif data[0] != 255:
            # TODO: Add custom exception
            raise Exception('Incorrect response')

        payload = data[3:].decode('utf-16be').split('\x00')
        motd = await self.formatting(payload[3]).build_text()

        return {
            'protocol_version': payload[1],
            'server_version': payload[2],
            'motd': motd,
            'players': {
                'current': payload[4],
                'max': payload[5]
            },
            'elapsed_time': end - start
        }
