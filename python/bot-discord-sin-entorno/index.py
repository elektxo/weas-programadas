import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='€', description="Este es el bot de fuentes")

@bot.command()
async def guillermina(ctx):
    await ctx.send('donde esta alfredito?')


@bot.command()
async def programeitor(ctx):
    ctx.send('guille deja de programar coñooooo')

@bot.event
async def on_ready():
    print('Esto funciona')

bot.run('820248417615740939')