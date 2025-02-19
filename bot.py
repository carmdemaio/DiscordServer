from keepAlive import keep_alive  # ✅ Import the keep_alive function
import discord
import os

# Load the bot token from Replit Secrets
TOKEN = os.getenv(
    "YOUR_BOT_TOKEN_HERE")  # Fetch token from Replit Secrets Vault
print(f"🔑 Loaded token: {TOKEN[:5]}********")
if not TOKEN:
    raise ValueError(
        "❌ ERROR: YOUR_BOT_TOKEN_HERE is not set in Replit Secrets!")

intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages
bot = discord.Client(intents=intents)

# Define emoji-to-role mappings (You can expand this)
EMOJI_ROLE_MAP = {
    "🐋": "Sea of Thieves",  # Whale emoji -> Sea of Thieves role
    "🦗": "Helldivers 2",  # Eagle emoji -> Helldivers role
    "🧟": "Day Z",  # Zombie emoji -> Day Z role
    "🗺️": "Civ"  # Map emoji -> Civilization role
}


@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")


# ✅ Call keep_alive() before running the bot
keep_alive()


@bot.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return

    # Check for emojis in message
    for emoji, role_name in EMOJI_ROLE_MAP.items():
        if emoji in message.content:
            # Find the role in the server
            role = discord.utils.get(message.guild.roles, name=role_name)
            if role:
                await message.channel.send(
                    f"{role.mention} 🚨 {message.author} used {emoji}!")
            else:
                await message.channel.send(f"⚠️ Role '{role_name}' not found!")


bot.run(TOKEN)
