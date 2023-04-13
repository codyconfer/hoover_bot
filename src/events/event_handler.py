from abc import ABC
from logging import Logger, getLogger
from discord.ext import commands


class EventHandler(ABC):
    bot: commands.Bot
    log: Logger

    def __init__(self, _bot: commands.Bot):
        self.bot = _bot
        self.log = getLogger()
