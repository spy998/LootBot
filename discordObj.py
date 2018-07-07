import Lootbot, discord, json, atexit, logging
from discord.ext import commands


botDescription = 'Lootbot is intended as a tool for dungeon masters to use in addition to using loot tables'
lootbot = commands.Bot(command_prefix = '$$', description = botDescription)
  
@lootbot.event
async def on_ready():
    logger.info('Logged in as\nUsername:'+ bot.user.name + '\nID:' + '\n')


@lootbot.listen()
async def read_in():
    return "user input as string"

@lootbot.command()
async def roll(ctx):
    pass

def on_exit():
    pass

if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger(__name__)
    try:
        print("----------------------\n","LootBot","----------------------\n")
        logger.info('Checking Config')
        print("checking config \n")#check for user settings if it exists confirm info else ask for it
        print("initializing \n")#set object variables here give fail message if there is an issue
        print("successfully started LootBot")
        atexit.register(on_exit())
    except ValueError as error:
        pass
    except SystemExit as error:
        pass