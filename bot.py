# Work with Python 3.6
import discord
import os
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=(('%', '$')), description='Wiggly Bot')
  
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    await bot.process_commands(message)
        

#tells me the bot is open and loads cogs
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    cogs = ['cogs.catch']
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception:
            print(f'Couldn\'t load cog {cog}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.run(str(os.environ.get('TOKEN'))))
