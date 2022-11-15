import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')

intents=discord.Intents(guild_messages=True)
client=discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.get_channel()