import Lootbot
import discord
from discord.ext import commands

class discordDriver:

    botDescription = 'Lootbot is intended as a tool for dungeon masters to use in addition to using loot tables'
    bot = commands.Bot(command_prefix = '~', description = botDescription)
    def __init__(self):
        pass

    def readIN():
        return "user input as string"

class threadHandler:
    #In the offchance that threads are used
    pass

if __name__ == "__main__":
    print("----------------------\n","LootBot","----------------------\n")
    print("checking config \n")#check for user settings if it exists confirm info else ask for it
    print("initializing \n")#set object variables here give fail message if there is an issue
    print("successfully started LootBot")