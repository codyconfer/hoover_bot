import logging
from discord.ext import commands
from discord.message import Message
from action_handler import ActionHandler
from actions.sort_links import SortLinks
from channels import general_id
from console import COLORS, contextualize

log = logging.getLogger()


class OnMessage(ActionHandler):
    msg: Message

    def __init__(self, _bot: commands.Bot, message: Message):
        super().__init__(_bot)
        self.msg = message

    def match_response(self):
        match self.msg.content.lower():
            case "$hello":
                return "Hello!"
            case n if "hitler" in n:
                return "HITLER!"

    async def action(self):
        if self.msg.author == self.bot.user:
            log.debug("message is from bot")
            return
        response = self.match_response()
        if response and len(response):
            log.info(f"sending {contextualize(response, COLORS.Yellow)} to {contextualize(self.msg.channel.name, COLORS.Cyan)}")
            await self.msg.channel.send(response)
        if self.msg.channel.id == general_id:
            await SortLinks(self.bot, self.msg).action()
        await self.bot.process_commands(self.msg)
