def parseSub(self, msg):
    splitMsg = msg.content.split()

    if (len(splitMsg) == 1):
        

    if (len(splitMsg) > 1):
        requestedRole = message.content.split(' ', 1)[1]
        foundRole = None

        for role in message.guild.roles:
            if (requestedRole.lower() == role.name.lower() and role.permissions.value == 0 and role.mentionable and not role.is_default()):
                foundRole = role
                break

        if (foundRole):
            if (foundRole in message.author.roles):
                response += str(message.author.name) + ": You are already subscribed to " + str(foundRole.name)
            else:
                await message.author.add_roles(foundRole)
                response += str(message.author.name) + ": You have been subscribed to " + str(foundRole.name)
        else:
            response += str(message.author.name) + ": Role " + str(requestedRole) + " was not found."

def displaySubRoles(self):
    response += str(message.author.name) + ": The available subscriptions are — "
        for role in message.guild.roles:
            if (role.permissions.value == Permission_Type.No_Permissions.value and role.mentionable and not role.is_default()):
                response += role.name + ", "