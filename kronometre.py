import discord
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def Kronometre(ctx, sure = 5):
    await ctx.send(f"Tabii, {sure} saniyelik kronometreyi başlattım!")
    time.sleep(sure)
    await ctx.send("Süre bitti!")

bot.run("token")
