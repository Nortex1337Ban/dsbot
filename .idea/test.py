import discord
from discord.ext import commands

TOKEN = ''
PREFIX = '>'
intents = discord.Intents().all()

bot = commands.Bot(command_prefix = PREFIX, intents = intents)

@bot.command()
async def hello(ctx):
    await ctx.reply('hello')

bot.run(TOKEN)##