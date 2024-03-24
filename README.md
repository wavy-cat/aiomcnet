# aiomcnet

An asynchronous Python library for interacting with Minecraft servers.

This library is under active development, so it can change dramatically.

## Installing

Download the repository code archive and copy the `aiomcnet` folder to your project.
So far this is the only way to install the library. It will be uploaded to PyPI in the future.

## Quick start

Import the `Server` class from the `aiomcnet` library and use its methods such as `.ping()` to work with it.

```python
import asyncio
from aiomcnet import Server


async def get_server(address, port):
    serv = Server(host=address, port=port, timeout=5)
    status = await serv.ping()
    print(status)  # This will output all values as a JSON string.
    print(dict(status))  # This will output all the values in the form of a dictionary.


asyncio.run(get_server('play.cubecraft.net', 25565))
```

## Formatting

Formatting is provided for convenience when working with Minecraft color codes, if needed.
Formatting is used for:
* MOTD text (in the ping method)
* Message text (soon in RCON method)

Built-in Types:

* `AbcFormat` - Abstract class
* `TerminalFormat` - Replaces Minecraft color codes with ANSI control sequences for color display in the terminal.
* `AmpersandFormat` - Replaces a paragraph character with an ampersand character.
* `ClearFormat` - Removes all formatting characters.

Example:

```python
from aiomcnet import Server, formatting


async def get_server_with_formatting(address):
    """Output to the MOTD server console with the TerminalFormat format type."""
    serv = Server(address, formatting=formatting.TerminalFormat)
    status = await serv.ping()
    print(status.motd)
```

## TODO

| Functionality  | Status      |
|----------------|-------------|
| Ping           | In Progress |
| Query          | Planned     |
| RCON           | Planned     |
| Ping Bedrock   | Planned     |
