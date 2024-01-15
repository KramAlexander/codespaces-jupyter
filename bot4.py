import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())
with open('token.txt') as file:
    token = file.readlines()

@bot.event
async def on_ready():
    print("Bot is up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hey")


bot.run(token[0])