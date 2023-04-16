import discord
from discord.ext.commands import Context
from discord.ext import commands
from discord.message import Message
from config import CONFIG, configure_logging
from commands.clean import Clean
from events.on_message import OnMessage
from events.on_ready import OnReady

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


bot.run(CONFIG.TOKEN)
