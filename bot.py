import discord
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your bot's token
TARGET_EMOJI = "🔥"  # Replace with the emoji you want to trigger the ping

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Required for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore bot messages

    if TARGET_EMOJI in message.content:
        await message.channel.send(f"@everyone 🚨 {message.author} used {TARGET_EMOJI}!")

bot.run(TOKEN)
