import logging
import re
from discord.ext.commands import Context, Bot
from discord.ext import commands
from discord.message import Message
from action_handler import ActionHandler
from console import COLORS, contextualize
from channels import (
    match_map,
    spotify_id,
    bot_testing_id,
    history_limit,
)

log = logging.getLogger()


class SortLinks(ActionHandler):
    message: Message

    def __init__(self, _bot: commands.Bot, _message: Message):
        super().__init__(_bot)
        self.message = _message

    async def action(self):
        msg = self.message.content
        _, spotify_urls = self.match_url(spotify_id, msg)
        if len(spotify_urls):
            new_urls = await self.check_repost(spotify_id, spotify_urls)
            if len(new_urls):
                await self.post_new_urls(new_urls)
            else:
                log.info("no new spotify urls")

    async def post_new_urls(self, new_urls: set):
        message_header = f"\n *recommendation by* {self.message.author.mention}\n"
        message_urls = str.join("\n", new_urls)
        response = f"{message_header} > {message_urls}"
        bot: Bot = self.bot
        channel = bot.get_channel(spotify_id)
        log.info(f"sending to {contextualize(channel.name, COLORS.Cyan)}")
        log.info(f"{response}")
        await channel.send(response)

    @staticmethod
    def match_url(key: int, msg: str):
        url_rexp = "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
        msg_match = re.search(url_rexp, msg)
        urls = []
        if msg_match:
            for segment in msg.split(' '):
                segment_match = re.search(url_rexp, segment)
                if segment_match and match_map[key] in segment:
                    urls.append(segment)
        return msg_match, urls

    async def check_repost(self, key: int, general_urls: []):
        match key:
            case spotify_id:
                return await self.check_channel_history(spotify_id, general_urls)

    async def check_channel_history(self, key: int, general_urls: []):
        bot: Bot = self.bot
        channel = bot.get_channel(key)
        messages = [item async for item in channel.history(limit=history_limit)]
        sorted_urls = []
        for msg in messages:
            url_match, match_urls = self.match_url(key, msg.content)
            if url_match:
                sorted_urls.extend(match_urls)
        new_urls = []
        for url in general_urls:
            if url not in sorted_urls:
                new_urls.append(url)
        return set(new_urls)
