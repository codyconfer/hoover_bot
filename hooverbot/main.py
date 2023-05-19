import discord
from discord.ext.commands import Context
from discord.ext import commands
from discord.message import Message
from prometheus_client import start_http_server
from config import CONFIG, configure_logging
from hooverbot.handlers.commands.clean import Clean
from hooverbot.handlers.events.on_message import OnMessage
from hooverbot.handlers.events.on_ready import OnReady

log = configure_logging()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    await OnReady(bot).action()


@bot.event
async def on_message(message: Message):
    await OnMessage(bot, message).action()


@bot.command(name="clean")
async def clean(ctx: Context):
    await Clean(bot, ctx).action()


if __name__ == "__main__":
    start_http_server(9090)
    bot.run(CONFIG.TOKEN)
