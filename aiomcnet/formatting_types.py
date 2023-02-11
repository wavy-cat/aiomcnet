class NoneFormat:
    def __init__(self, text: str):
        self.text = text

    async def build_text(self):
        return self.text


class AmpersandFormat(NoneFormat):
    def __init__(self, text: str):
        super().__init__(text)

    async def build_text(self):
        return self.text.replace('§', '&')


class TerminalFormat(NoneFormat):
    def __init__(self, text: str):
        super().__init__(text)

    async def build_text(self):
        return self.text.replace('§0', '\033[30m')\
            .replace('§1', '\033[34m')\
            .replace('§2', '\033[32m')\
            .replace('§3', '\033[36m')\
            .replace('§4', '\033[31m')\
            .replace('§5', '\033[35m')\
            .replace('§6', '\033[33m')\
            .replace('§7', '\033[37m')\
            .replace('§8', '\033[90m')\
            .replace('§9', '\033[94m')\
            .replace('§a', '\033[92m')\
            .replace('§b', '\033[96m')\
            .replace('§c', '\033[91m')\
            .replace('§d', '\033[95m')\
            .replace('§e', '\033[93m')\
            .replace('§f', '\033[97m')\
            .replace('§k', '\033[8m')\
            .replace('§l', '\033[1m')\
            .replace('§m', '\033[9m')\
            .replace('§n', '\033[4m')\
            .replace('§o', '\033[3m')\
            .replace('§r', '\033[0m') + '\033[0m'


class ColoramaFormat(NoneFormat):
    def __init__(self, text: str):
        super().__init__(text)

    async def build_text(self):
        from colorama import Fore, Style

        return self.text.replace('§0', Fore.BLACK) \
            .replace('§1', Fore.BLUE) \
            .replace('§2', Fore.GREEN) \
            .replace('§3', Fore.CYAN) \
            .replace('§4', Fore.RED) \
            .replace('§5', Fore.MAGENTA) \
            .replace('§6', Fore.YELLOW) \
            .replace('§7', Fore.BLACK) \
            .replace('§8', Fore.BLACK) \
            .replace('§9', Fore.LIGHTBLUE_EX) \
            .replace('§a', Fore.LIGHTGREEN_EX) \
            .replace('§b', Fore.LIGHTCYAN_EX) \
            .replace('§c', Fore.LIGHTRED_EX) \
            .replace('§d', Fore.LIGHTMAGENTA_EX) \
            .replace('§e', Fore.LIGHTYELLOW_EX) \
            .replace('§f', Fore.WHITE) \
            .replace('§k', '') \
            .replace('§l', Style.BRIGHT) \
            .replace('§m', Style.DIM) \
            .replace('§r', Style.RESET_ALL + Fore.RESET) + Style.RESET_ALL + Fore.RESET
