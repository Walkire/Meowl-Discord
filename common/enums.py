from enum import Enum

class Command_Type(Enum):
    sub = '?sub'
    unsub = '?unsub'

class Permission_Type(Enum):
    No_Permissions = 0
