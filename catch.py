import discord
from discord import File
from discord.ext import commands

class Catch(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    gm_dict={}
    with open("valuesGMAX.txt", 'r') as f:
        for line in f:
            items = line.split('/')
            key, values = items[0], items[1:]
            gm_dict[key] = values

    norm_dict={}
    with open("values.txt", 'r') as f:
        for line in f:
            items = line.split('/')
            key, values = items[0], items[1:]
            norm_dict[key] = values

    @commands.command()
    async def ball(self, ctx, arg1 = None, arg2 = None):
        if arg1 == None:
            msg = ('Invalid input!')

        elif arg1 != None and arg2 == None:
            pk = arg1.capitalize()

            if pk not in self.norm_dict:
                msg = "Pokemon not found!"

            else:
              msga = 'Here are the ball catch rates for ' + pk
              msgb = '\n'.join(map(str, self.norm_dict.get(pk)))
              msg = msga + ':\n' + msgb
              msg += "\n"
              msg += "Please note that these values may not be completely correct!"

        elif arg1 == 'g' or arg1 == 'G' and arg2 != None:
            pk = arg2.capitalize()

            if pk not in self.gm_dict:
                msg="Pokemon not found!"

            else:
                msga = 'Here are the ball catch rates for Gigantamax ' + pk
                msgb = '\n'.join(map(str, self.gm_dict.get(pk)))
                msg = msga + ':\n' + msgb
                msg += "\n"
                msg += "Please note that these values may not be completely correct!"

        await ctx.send(msg)

    @commands.command()
    async def wiggly(self, ctx):
        await ctx.send(file = File('wiggly.png'))


def setup(bot):
    bot.add_cog(Catch(bot))