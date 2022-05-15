from dotenv import load_dotenv
from discord.ext import commands
import os
import discord

load_dotenv()

TOKEN = os.environ.get(["TOKEN"])

client = commands.Bot(command_prefix=".")

# Bot information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Starts the bot
client.run(TOKEN)