import discord
from discord.ext import commands

from dbot.controller.client import SendVideoToYoutubeCliente
from dbot.controller.command import upload

intents=discord.Intents.default()
intents.message_content = True

def init_client(token):
    client = SendVideoToYoutubeCliente(intents=intents)
    client.run(token)

def init_command(token):
    bot = commands.Bot(command_prefix='/', intents=intents)
    bot.add_command(upload)
    bot.run(token)

def init(start):
    return eval(f'init_{start}')