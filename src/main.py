import logging
import discord
from discord.ext import commands
from config import CONFIG
from events.on_message import OnMessage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s |  %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
log = logging.getLogger()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    log.info(f"{bot.user} has connected to Discord!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        log.info("message is from bot")
        return
    handler = OnMessage(bot)
    await handler.handle_hello(message)


bot.run(CONFIG.TOKEN)
