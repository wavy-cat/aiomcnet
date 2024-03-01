#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import asyncio
from typing import Optional, Type
from aiomcnet.formatting import AbcFormat
from aiomcnet.objects.ping import PingResponse


class Server:
    def __init__(self, host: str, port: int = 25565, *,
                 timeout: int = 60, formatting: Optional[Type[AbcFormat]] = None):
        if timeout <= 0:
            raise AttributeError('The timeout cannot be less than or equal to zero.')

        if formatting and not issubclass(formatting, AbcFormat):
            raise AttributeError('The formatting class should be a subclass of aiomcnet.formatting.AbcFormat.')

        self.host = host
        self.port = port
        self.timeout = timeout
        self.formatting = formatting

    async def ping(self, read_bits: int = 2048) -> PingResponse:
        """
        Send a ping request to the server.

        :param read_bits: The number of bits to read from the server. Default is 2048.
        :type read_bits: int
        :return: The PingResponse object containing ping information.
        :rtype: PingResponse
        :raises TimeoutError: If the ping request times out.
        :raises ConnectionError: If the server does not respond or the response is incorrect.
        """

        start = asyncio.get_running_loop().time()
        reader, writer = await asyncio.open_connection(self.host, self.port)

        writer.write(b'\xfe\x01')
        await writer.drain()

        task = asyncio.create_task(reader.read(read_bits))
        done, pending = await asyncio.wait({task}, timeout=self.timeout)

        if task in done:
            data = task.result()
            writer.close()
        else:
            writer.close()
            raise TimeoutError('Timeout')

        end = asyncio.get_running_loop().time()

        if not data:
            raise ConnectionError('The server did not respond')
        elif data[0] != 255:
            raise ConnectionError('Incorrect response')

        payload = data[3:].decode('utf-16be').split('\x00')
        motd = self.formatting(payload[3]).format_text if self.formatting else payload[3]

        return PingResponse(int(payload[1]), payload[2], motd, int(payload[4]), int(payload[5]), end - start)

    async def query(self, port: int = None):
        port = self.port if not port else port


