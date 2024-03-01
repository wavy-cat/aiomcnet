#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import json


class PingResponse:
    """
    The `PingResponse` class represents a response object received from a ping request to a server. It contains
    information about the protocol version, server version, MOTD, current players, maximum players and elapsed time.

    Attributes:
        protocol_version (int): The protocol version of the server.
        server_version (str): The version of the server software.
        motd (str): The message of the day displayed by the server.
        players (dict): A dictionary containing information about the current and maximum number of players.
        elapsed_time (float): The elapsed time in seconds for the ping request.

    Methods:
        __init__(protocol_version: int, server_version: str, motd: str,
                 players_current: int, players_max: int, elapsed_time: float):
            Initializes a new instance of the `PingResponse` class. Assigns the provided values to the corresponding attributes.

        __str__():
            Returns a string representation of the `PingResponse` object, including the values of all attributes.
    """

    def __init__(self, protocol_version: int, server_version: str, motd: str,
                 players_current: int, players_max: int, elapsed_time: float):
        self.protocol_version = protocol_version
        self.server_version = server_version
        self.motd = motd
        self.players = {'current': players_current, 'max': players_max}
        self.elapsed_time = elapsed_time

    def __str__(self):
        return json.dumps({'protocol_version': self.protocol_version, 'server_version': self.server_version,
                           'motd': self.motd, 'players': self.players, 'elapsed_time': self.elapsed_time})

    def __len__(self):
        # Returns the amount players on the server.
        return self.players['current']

    def __iter__(self):
        attributes = ("protocol_version", "server_version", "motd", "players", "elapsed_time")
        for attribute in attributes:
            yield attribute, getattr(self, attribute)
