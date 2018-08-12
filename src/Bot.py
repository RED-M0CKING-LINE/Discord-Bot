from Secrets import BOT_TOKEN

import discord
from discord.ext import commands
import asyncio
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='logs/discordBot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s: %(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix=',')


#TODO IMPLEMENT JSON USAGE FOR STORING VALUES SUCH AS WHO CAN USE SPECIFIC COMMANDS IN EACH SERVER AND CUSTOM PREFIXES

@bot.event
async def on_ready():
    logger.info('THE BOT HAS STARTED')
    print('===== BOT IS READY =====')
    print('===== RUNNING ON: ' + str(bot.user.name) + ' =====')
    print('===== BOT ID IS: ' + str(bot.user.id) + ' =====')


@bot.command(pass_context=True)
async def ping():
    await bot.say('Pong!')


@bot.command(pass_context=True)
async def user(ctx, usr: discord.Member):
    await bot.say('User: {}'.format(usr.name))
    await bot.say('User ID: {}'.format(usr.id))
    await bot.say('User is: {}'.format(usr.status))
    await bot.say('User\'s highest role: {}'.format(usr.top_role))
    await bot.say('User Joined {}'.format(usr.joined_at))
    await bot.say('Bot will shutdown by command of {}'.format(usr.name))


@bot.command(pass_context=True)
async def shutdown(ctx):
    await bot.say('Bot will shutdown by command of {0.author.mention}'.format(ctx.message))


bot.run(BOT_TOKEN.BOT_TOKEN)
