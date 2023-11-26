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
            case s if "tebow" in s:
                return "https://cdn.discordapp.com/attachments/1095041572917227612/1178074884102950953/image0.gif?ex=6574d2bb&is=65625dbb&hm=573d7776b74b3e0a218f1ff0b91b789af60af0807d9b85890c1e67bbf5cb2431&"
            case s if "sabin" in s:
                return "https://tenor.com/view/nick-saban-roll-tide-angry-gif-15695210"
            case s if "china" in s:
                return "https://miro.medium.com/v2/resize:fit:748/format:webp/1*73DTaU64tQ4kv1d6fRl_GA.png"
            case s if "hitler" in s:
                return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4LZhgvo78i0cGaZq_U7R_xJhnTkkhTcZLYg&usqp=CAU"
            case s if "chemtrails" in s:
                return "https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1687,w_3000,x_0,y_0/dpr_1.5/c_limit,w_1044/fl_lossy,q_auto/v1570465280/191007-weill-chemtrails-greta-tease_g99nr3"
            case s if "biden" in s:
                return "https://media.discordapp.net/attachments/1153384689298591785/1166544272078684170/image0.jpg?ex=654ae003&is=65386b03&hm=dd668f0230d2a5dc00ee74aab58609d8e4c307a7466f71cbe8e50b30cd948fc4&=&width=1130&height=1124"
            case s if "420" in "".join(filter(str.isalnum, s)):
                return "Blaze it!"
            case s if "4" in s and "20" in s:
                return "Blaze it!"
            case s if "69" in "".join(filter(str.isalnum, s)):
                return "https://media0.giphy.com/media/26gspipWnu59srmM0/giphy.gif?cid=ecf05e47z383wujy8jqne6pzwx7u70vt69rdk12v00gjljbl&ep=v1_gifs_search&rid=giphy.gif&ct=g"
            case s if "april showers bring may flowers" in s:
                return "...and the mayflower brought way too many fucking white people"
            case s if "bot wildin" in s:
                return "we out here!"
            case s if "gimme dat" in s:
                return "https://media.tenor.com/aQdtUhPzrNQAAAAC/itysl-gimme.gif"
            case s if "gimmie dat" in s:
                return "https://media.tenor.com/aQdtUhPzrNQAAAAC/itysl-gimme.gif"
            case s if "gimme that" in s:
                return "https://media.tenor.com/aQdtUhPzrNQAAAAC/itysl-gimme.gif"
            case s if "gimmie that" in s:
                return "https://media.tenor.com/aQdtUhPzrNQAAAAC/itysl-gimme.gif"

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
