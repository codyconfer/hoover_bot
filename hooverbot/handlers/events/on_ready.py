import logging
from discord.ext import commands
from hooverbot.handlers.handler import Handler
from hooverbot.logger.console import COLORS, contextualize

log = logging.getLogger()


class OnReady(Handler):
    def __init__(self, _bot: commands.Bot):
        super().__init__(_bot)

    async def action(self):
        log.info(
            f"{contextualize(self.bot.user.name, COLORS.Bright_Magenta)} has connected to Discord!"
        )
