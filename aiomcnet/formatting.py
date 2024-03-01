#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from abc import ABC, abstractmethod
import re


class AbcFormat(ABC):
    """
    The AbcFormat class is an abstract base class that defines the interface for formatting text.

    :param text: The source text to be formatted.
    :type text: str
    """

    def __init__(self, text: str, /):
        self.source_text = text

    @property
    @abstractmethod
    def format_text(self):
        pass


class AmpersandFormat(AbcFormat):
    """
    Implements the AmpersandFormat class that inherits from the AbcFormat class.
    This class provides a method to format text and replace all occurrences of '§' with '&'.

    :param text: The input text to be formatted.
    :type text: str
    """

    def __init__(self, text: str, /):
        super().__init__(text)

    @property
    def format_text(self):
        return self.source_text.replace('§', '&')


class ClearFormat(AbcFormat):
    """
    Implements the ClearFormat class that inherits from the AbcFormat class.
    This class provides the functionality to remove all occurrences of '§' in the input text.

    :param text: The input text to be formatted.
    :type text: str
    """

    def __init__(self, text: str, /):
        super().__init__(text)

    @property
    def format_text(self):
        return re.sub('§.', '', self.source_text)


class TerminalFormat(AbcFormat):
    """
    Implements the TerminalFormat class that inherits from the AbcFormat class.
    This class provides formatting functionality for terminal output.

    :param text: The input text to be formatted.
    :type text: str
    """

    def __init__(self, text: str, /):
        super().__init__(text)

    @property
    def format_text(self):
        marks = {'§1': '\033[34m', '§2': '\033[32m', '§3': '\033[36m', '§4': '\033[31m', '§5': '\033[35m',
                 '§6': '\033[33m', '§7': '\033[37m', '§8': '\033[90m', '§9': '\033[94m', '§a': '\033[92m',
                 '§b': '\033[96m', '§c': '\033[91m', '§d': '\033[95m', '§e': '\033[93m', '§f': '\033[97m',
                 '§k': '\033[8m', '§l': '\033[1m', '§m': '\033[9m', '§n': '\033[4m', '§o': '\033[3m', '§r': '\033[0m'}
        text = self.source_text

        for symbol, escape_sequence in marks.items():
            text = text.replace(symbol, escape_sequence)

        return text + '\033[0m'
