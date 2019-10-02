# Work with Python 3.6
import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_message(message):
    msg = ""
    
    # we do not want the bot to reply to itself or other bots
    if message.author.bot:
        return

    if message.content.startswith('?sub'):
        msg += str(message.author.name) + ": The available subscriptions are — "
        for role in message.guild.roles:
            if (role.mentionable and not role.is_default()):
                msg += role.name + ", "
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv("DISCORD_BOT_TOKEN"));