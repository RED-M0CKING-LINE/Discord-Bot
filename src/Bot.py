from Secrets import BOT_TOKEN

import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discordBot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s: %(name)s: %(message)s'))
logger.addHandler(handler)


#def get_prefix(bot, message):  # Get the prefix for the bot
    #extras = MessageProcessing.prefixes_for(message.guild, bot.prefix_data)
    #return commands.when_mentioned_or(*extras)(bot, message)


class Bot(commands.Bot):

    #def __init__(self):
        #super().__init__(command_prefix=get_prefix, case_insensitive=True)

    async def on_message(self, message):
        if not message.author.bot:
            ctx = await bot.get_context(message)
            await self.invoke(ctx)


bot = Bot(",")
bot.run(BOT_TOKEN.BOT_TOKEN)
