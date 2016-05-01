import discord
from discord.ext import commands
import random

#import httplib extensions
import requests      

import settings

description = '''An example bot to showcase the discord module'''

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('----------')

@bot.command()
async def add(left : int, right : int):
        """Adds two numbers together."""
        await bot.say(left + right)

@bot.command()
async def roll(dice: str):
        """Rolls a dice in NdN format."""
        try:
                rolls, limit = map(int, dice.split('d'))
        except Exception:
                await bot.say('Format has to be NdN')
                return
        
        result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
        await bot.say(result)

@bot.command(description='For when you wanna settle the score another way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """

    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot cool.')


#query discord to get token
r=requests.post('https://discordapp.com/api/auth/login'), 

print ("Hello World")

bot.run(settings.username,settings.password)

        

