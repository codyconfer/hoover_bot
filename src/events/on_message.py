from .event_handler import EventHandler
from discord.ext import commands


class OnMessage(EventHandler):
    def __init__(self, _bot: commands.Bot):
        super().__init__(_bot)

    async def handle_hello(self, message):
        self.log.info(f"{self.bot.user.name} handling hello.")
        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")
