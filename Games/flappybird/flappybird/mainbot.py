# imports and extensions
import discord.utils
import discord
from discord.ext import commands
import pygame
import random
import flappy

# bot declaration
bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())
# opening token from token.txt
with open('token2.txt') as file:
    token = file.readlines()

#start-message of bot
@bot.event
async def on_ready():
    print("Dark Clydé is online")
    try:
        synced = await bot.tree.sync()
        print(f"ou can use {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="play")
async def play(interaction: discord.Interaction):
    flappy.flappybirds()
    await interaction.response.send_message("Have fun")
    

# running bot with token
bot.run(token[0])

