import discord
from discord.ext import commands
import os
import asyncio
import nest_asyncio

nest_asyncio.apply()

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
async def main():
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))
    await bot.run("MTA0ODk2NDEyOTQwNDIzNTgwNg.GhVD77.Yms-t0c91n_oHGehe50BSK_YA5axZHV43vE6_0")

asyncio.run(main())

