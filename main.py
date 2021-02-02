# Work with Python 3.6
import discord
import os
import controller.commands as Meowl
from common.enums import Command_Type 
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself or other bots
    if message.author.bot:
        return

    user = message.author
    server = message.guild
    channel = message.channel
    text = message.content

    splitMsg = text.split()
    requestedCommand = splitMsg[0].lower()

    #sub
    if requestedCommand == Command_Type.sub.value:
        if (len(splitMsg) == 1):
            await Meowl.displayRoles(user, server.roles, channel)
        if (len(splitMsg) > 1):
            await Meowl.giveRole(user, text, server.roles, channel)

    #unsub
    if requestedCommand == Command_Type.unsub.value:
        await Meowl.removeRole(user, text, server.roles, channel)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv("DISCORD_BOT_TOKEN"))