# Work with Python 3.6
import discord
import os
from common.enums import Command_Type 
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_message(message):
    response = ""
    requestedCommand = message.content.split(' ')[0].lower()
    # we do not want the bot to reply to itself or other bots
    if message.author.bot:
        return

    if requestedCommand == Command_Type.sub.value:

    if requestedCommand == Command_Type.unsub.value:
        splitMsg = message.content.split()
        foundRole = Nones
        
        if (len(splitMsg) > 1):
            requestedRole = message.content.split(' ', 1)[1]
            for role in message.guild.roles:
                if (requestedRole.lower() == role.name.lower() and role.permissions.value == Permission_Type.No_Permissions.value and role.mentionable and not role.is_default()):
                    foundRole = role
                    break

            if (foundRole):
                if (foundRole in message.author.roles):
                    await message.author.remove_roles(foundRole)
                    response += str(message.author.name) + ": You have been unsubscribed to " + str(foundRole.name)
                else:
                    response += str(message.author.name) + ": You are not subscribed to " + str(foundRole.name)
            else:
                response += str(message.author.name) + ": Role " + str(requestedRole) + " was not found."
        else:
            response += str(message.author.name) + ": Role was not found."
            
    if (response):
        await message.channel.send(response)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv("DISCORD_BOT_TOKEN"))