import logging
from discord.ext import commands
from discord.message import Message
from hooverbot.handlers.handler import Handler
from hooverbot.handlers.actions.sort_links import SortLinks
from hooverbot.channels import general_id
from hooverbot.logger.log_formatters import log_response, log_incoming

log = logging.getLogger()


class OnMessage(Handler):
    msg: Message

    def __init__(self, _bot: commands.Bot, message: Message):
        super().__init__(_bot)
        self.msg = message

    def match_response(self):
        match self.msg.content.lower():
            case "$hello":
                return "Hello!"
            case s if "hitler" in s:
                return "HITLER!"
            case s if "420" in "".join(filter(str.isalnum, s)):
                return "Blaze it!"
            case s if "4" in s and "20" in s:
                return "Blaze it!"
            case s if "april showers bring may flowers" in s:
                return "...and the mayflower brought way too many fucking white people"
            case s if "bot wildin" in s:
                return "we out here!"

    async def action(self):
        if self.msg.author == self.bot.user:
            log.debug("message is from bot")
            return
        log.info(
            log_incoming(self.msg.channel.name, self.msg.author.name, self.msg.content)
        )
        response = self.match_response()
        if response and len(response):
            log.info(log_response(self.msg.channel.name, self.bot.user.name, response))
            await self.msg.channel.send(response)
        if self.msg.channel.id == general_id:
            await SortLinks(self.bot, self.msg).action()
        await self.bot.process_commands(self.msg)
