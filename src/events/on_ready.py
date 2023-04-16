import logging
from discord.ext import commands
from discord.message import Message
from action_handler import ActionHandler
from console import COLORS, contextualize

log = logging.getLogger()


class OnReady(ActionHandler):
    def __init__(self, _bot: commands.Bot):
        super().__init__(_bot)

    async def action(self):
        log.info(f"{contextualize(self.bot.user.name, COLORS.Bright_Magenta)} has connected to Discord!")
