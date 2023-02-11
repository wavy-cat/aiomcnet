# aiomcnet
An asynchronous Python library for interacting with Minecraft servers.

This library is under active development, so it can change dramatically.

## Examples
### Ping
```python
import asyncio
from aiomcnet import client

async def main(address):
    serv = client.Client(timeout=5)
    status = await serv.ping(address, port=25565)
    print(status)

asyncio.run(main('play.cubecraft.net'))
```

### Ping with text formatting
```python
import asyncio
from aiomcnet import client, formatting_types

async def main(address):
    serv = client.Client(timeout=5, formatting=formatting_types.AmpersandFormat)
    status = await serv.ping(address, port=25565)
    print(status)
    print(status['motd'])

asyncio.run(main('play.cubecraft.net'))
```

## Formatting

Formatting is needed to work with Minecraft color codes. For example, in ping it is needed to change the MOTD.

Built-in Types:
* NoneFormat (parent class) - doesn't change anything.
* TerminalFormat (default) - Replaces Minecraft color codes with Python color codes for display in the terminal.
* AmpersandFormat - Replaces a paragraph character with an ampersand character.
* ColoramaFormat - Same as TerminalFormat, but using the Colorama library.

## TODO

| Type  | Supported          |
|-------|--------------------|
| Ping  | :white_check_mark: |
| Query | :x:                |
| RCON  | :x:                |
