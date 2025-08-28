# This example requires the 'members' and 'message_content' privileged intents to function.
import random
import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=',',  intents=intents)




@bot.command()
async def add(ctx, left: int, right: int):

    await ctx.send(left + right)
@bot.command()
async def hola(ctx):
    await ctx.send("hola me llamo botsaso")
@bot.command()
async def  pregunta(ctx, cantidad):
    
    cantidad = int(cantidad)
    

    letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contraseña = "".join(random.choice(letras) for i in range(cantidad))
    await ctx.send(f"tu contraseña es {contraseña}")
@bot.command()
async def google(ctx):
    await ctx.send("https://www.google.com/")
@bot.command()
async def url(ctx, app):
    await ctx.send(f"https://{app}.com/")
@bot.command()
async def moneda(ctx):
    salida=random.randint(1,2)
    if salida==1:
        await ctx.send("cara")
    elif salida==2:

        await ctx.send("cruz")

bot.run('token')

