import logging
from discord.ext.commands import Context
from discord.ext import commands
from hooverbot.handlers.handler import Handler
from hooverbot.handlers.actions.sort_links import SortLinks
from hooverbot.channels import general_id, history_limit

log = logging.getLogger()


class Clean(Handler):
    ctx: Context

    def __init__(self, _bot: commands.Bot, _ctx: Context):
        super().__init__(_bot)
        self.ctx = _ctx

    async def action(self):
        channel = self.bot.get_channel(general_id)
        async for msg in channel.history(limit=history_limit):
            await SortLinks(self.bot, msg).action()
