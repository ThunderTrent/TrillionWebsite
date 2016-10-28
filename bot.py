import discord
from discord.ext import commands
import random
import subprocess

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def addToonToTrillionWebsite(characterName : str, characterServer : str):
    """Adds two numbers together."""
    await bot.say("Added " + characterName + " to Trillion Website Successfully.")

@bot.command()
async def updateRankings(characterName : str, characterServer : str):
    p = subprocess.Popen(['python','/Projects/trillionizer/manage.py', "addRankings", characterName, characterServer],
                                     stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
    results = p.stdout.read()

    await bot.say("Updated " + characterName + "'s Rankings on www.wearetrillion.com" + str(results))

@bot.command()
async def setNickname(characterName : str, nickName : str):
    p = subprocess.Popen(['python','/Projects/trillionizer/manage.py', "setNickname", characterName, nickName],
                                     stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
    results = p.stdout.read()

    await bot.say(str(results))


@bot.command()
async def setWebsiteNickname(characterName : str, nickname : str):
    """Adds two numbers together."""
    await bot.say("Updated " + characterName + "'s nickname to " + nickname + " for website display purposes.")


bot.run('MjM0MTcxMTY3Mzc4ODk4OTQ0.CtoIbQ.prvlNWqB_7KUO19x8tSTkKqgEYM')
