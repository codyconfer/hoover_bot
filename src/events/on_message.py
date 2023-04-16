import logging
from discord.ext import commands
from discord.message import Message
from action_handler import ActionHandler
from console import COLORS, contextualize

log = logging.getLogger()


class OnMessage(ActionHandler):
    msg: Message

    def __init__(self, _bot: commands.Bot, message: Message):
        super().__init__(_bot)
        self.msg = message

    def match_response(self):
        match self.msg.content:
            case "$hello":
                return "Hello!"

    async def action(self):
        if self.msg.author == self.bot.user:
            log.info("message is from bot")
            return
        response = self.match_response()
        if response and len(response):
            log.info(f"sending {response} to {contextualize(self.msg.channel.name, COLORS.Cyan)}")
            await self.msg.channel.send(response)
        await self.bot.process_commands(self.msg)
