import logging
import re
from discord.ext import commands
from discord.message import Message
from hooverbot.handlers.handler import Handler
from hooverbot.channels import (
    match_map,
    apple_music_id,
    spotify_id,
    soundcloud_id,
    youtube_id,
    bot_testing_id,
    history_limit,
)
from hooverbot.logger.log_formatters import log_response

log = logging.getLogger()


class SortLinks(Handler):
    message: Message

    def __init__(self, _bot: commands.Bot, _message: Message):
        super().__init__(_bot)
        self.message = _message

    async def action(self):
        msg = self.message.content
        _, spotify_urls = self.match_url(spotify_id, msg)
        await self.post_new_urls(spotify_id, spotify_urls)
        _, soundcloud_urls = self.match_url(soundcloud_id, msg)
        await self.post_new_urls(soundcloud_id, soundcloud_urls)
        _, youtube_urls = self.match_url(youtube_id, msg)
        await self.post_new_urls(youtube_id, youtube_urls)
        _, apple_music_urls = self.match_url(apple_music_id, msg)
        await self.post_new_urls(apple_music_id, apple_music_urls)

    async def post_new_urls(self, key: int, service_urls: []):
        if len(service_urls):
            new_urls = await self.check_repost(key, service_urls)
            if len(new_urls):
                response = self.build_message(new_urls)
                channel = self.bot.get_channel(key)
                log.info(log_response(channel.name, self.bot.user.name, response))
                await channel.send(response)

    def build_message(self, new_urls: []):
        message_header = f"\n *recommendation by* {self.message.author.mention}\n"
        message_urls = str.join("\n", new_urls)
        return f"{message_header} > {message_urls}"

    def match_url(self, key: int, msg: str):
        url_rexp = "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
        msg_match = re.search(url_rexp, msg)
        urls = []
        if msg_match:
            for segment in msg.split(" "):
                segment_match = re.search(url_rexp, segment)
                if segment_match and self.check_match_map(key, segment):
                    urls.append(segment)
        return msg_match, urls

    @staticmethod
    def check_match_map(key: int, segment: str):
        match_value = match_map[key]
        if isinstance(match_value, list):
            for value in match_value:
                if value in segment:
                    return True
            return False
        elif match_value in segment:
            return True
        else:
            return False

    async def check_repost(self, key: int, general_urls: []):
        channel = self.bot.get_channel(key)
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
