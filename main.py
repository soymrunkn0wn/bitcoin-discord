import discord # The main Discord.py library for interacting with Discord's API
from discord.ext import commands # Provides the commands framework for creating bot commands
import logging # For logging bot activities
from dotenv import load_dotenv # For loading environment variables from a .env file
import os # FOr accessing operating system functionality

load_dotenv() # Loads environment variables from the .env file
token = os.getenv('DISCORD_TOKEN') # Retrieves the Discord bot token from the .env file

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# This creates an intents object with Discord's default set of enabled intents. By default, this includes:
# Guild (server) information
# Basic member information
# Message reactions
# Typing indicators
intents = discord.Intents.default()

# This enables the bot to:
# Read the actual content of messages (required for command processing)
# See attachments, embeds, and other message content
# **Note**: This is a privileged intent and must be enabled in the Discord Developer Portal
intents.message_content = True

# This enables the bot to:
# Track member joins/leaves
# See full member lists
# Access richer member information
# This is also a privileged intent that must be enabled in the Developer Portal
intents.members = True

admin_role = "Admin"

# ! to type a command
bot = commands.Bot(command_prefix='!', intents=intents)

# This is called when the bot successfully connects to Discord
@bot.event
async def on_ready():
    print(f"We are ready to send & receive Bitcoin!, {bot.user.name}")

# This triggers when a new member joins any server your bot is in
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

# Add or remove banned words
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - Don't use that word!")

    await bot.process_commands(message)

# Starts and runs the Discord bot
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
