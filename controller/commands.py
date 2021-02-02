from common.enums import Permission_Type

async def displayRoles(user, roles, channel):
    res = ""
    res += str(user.name) + ": The available subscriptions are — "
    for role in roles:
        if (role.permissions.value == Permission_Type.No_Permissions.value and role.mentionable and not role.is_default()):
            res += role.name + ", "

    await channel.send(res)

async def giveRole(user, msg, roles, channel):
    requestedRole = msg.split(' ', 1)[1]
    foundRole = None
    res = ""

    for role in roles:
        if (requestedRole.lower() == role.name.lower() 
            and role.permissions.value == Permission_Type.No_Permissions.value 
            and role.mentionable 
            and not role.is_default()):
            foundRole = role
            break

    if (foundRole):
        if (foundRole in user.roles):
            res += str(user.name) + ": You are already subscribed to " + str(foundRole.name)
        else:
            await user.add_roles(foundRole)
            res += str(user.name) + ": You have been subscribed to " + str(foundRole.name)
    else:
        res += str(user.name) + ": Role " + str(requestedRole) + " was not found."

    await channel.send(res)

async def removeRole(user, msg, roles, channel):
    res = ""
    foundRole = None
    
    if (len(msg.split()) > 1):
        requestedRole = msg.split(' ', 1)[1]
        for role in roles:
            if (requestedRole.lower() == role.name.lower() 
                and role.permissions.value == Permission_Type.No_Permissions.value 
                and role.mentionable 
                and not role.is_default()):
                foundRole = role
                break

        if (foundRole):
            if (foundRole in user.roles):
                await user.remove_roles(foundRole)
                res += str(user.name) + ": You have been unsubscribed to " + str(foundRole.name)
            else:
                res += str(user.name) + ": You are not subscribed to " + str(foundRole.name)
        else:
            res += str(user.name) + ": Role " + str(requestedRole) + " was not found."
    else:
        res += str(user.name) + ": Role was not found."
    
    await channel.send(res)