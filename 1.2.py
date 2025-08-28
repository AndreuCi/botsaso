# This example requires the 'members' and 'message_content' privileged intents to function.
import random
import discord
from discord.ext import commands
import asyncio

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
async def pregunta(ctx, cantidad):
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
    salida = random.randint(1, 2)
    if salida == 1:
        await ctx.send("cara")
    elif salida == 2:
        await ctx.send("cruz")

@bot.command()
async def dado(ctx):
    salida = random.randint(1, 6)
    await ctx.send(salida)

@bot.command()
async def ayuda(ctx):
    await ctx.send("comandos: ,add ,hola ,pregunta ,google ,url ,moneda ,dado ,aleatorio ,ayuda, chinchanpoo")

@bot.command()
async def chinchanpoo(ctx, eleccion):
    eleccion = eleccion.lower()
    opciones = ["piedra", "papel", "tijeras"]
    if eleccion not in opciones:
        await ctx.send("Elección inválida. Por favor elige piedra, papel o tijeras.")
        return

    eleccion_bot = random.choice(opciones)
    await ctx.send(f"El bot eligió: {eleccion_bot}")

    if eleccion == eleccion_bot:
        await ctx.send("¡Empate!")
    elif (eleccion == "piedra" and eleccion_bot == "tijeras") or \
         (eleccion == "papel" and eleccion_bot == "piedra") or \
         (eleccion == "tijeras" and eleccion_bot == "papel"):
        await ctx.send("¡Ganaste!")
    else:
        await ctx.send("¡Perdiste!")

@bot.command()
async def adivinaelnumero(ctx):
    numero_secreto = random.randint(1, 100)
    intentos = 0
    await ctx.send("He elegido un número entre 1 y 100. ¡Adivina cuál es!")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        try:
            mensaje = await bot.wait_for('message', check=check, timeout=30.0)
            intento = int(mensaje.content)
            intentos += 1

            if intento < numero_secreto:
                await ctx.send("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                await ctx.send("Demasiado alto. Intenta de nuevo.")
            else:
                await ctx.send(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            await ctx.send("Por favor, ingresa un número válido.")
        except asyncio.TimeoutError:
            await ctx.send(f"Se acabó el tiempo. El número era {numero_secreto}.")
            break

@bot.command()
async def aleatorio(ctx, min: int, max: int):
    salida = random.randint(min, max)
    await ctx.send(salida)

bot.run('token')

