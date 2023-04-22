from abc import ABC, abstractmethod
import logging
from discord.ext import commands

log = logging.getLogger()


class Handler(ABC):
    bot: commands.Bot

    def __init__(self, _bot: commands.Bot):
        self.bot = _bot

    @abstractmethod
    def action(self):
        return
