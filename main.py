from dotenv import load_dotenv
from discord.ext import commands
import os
import discord

load_dotenv()

TOKEN = os.environ.get("TOKEN")

client = commands.Bot(command_prefix=".")

# Bot information
@client.event
async def on_ready():
    print(f"Connected to bot: {client.user.name}")
    print(f"Bot ID: {client.user.id}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Starts the bot
client.run(TOKEN)