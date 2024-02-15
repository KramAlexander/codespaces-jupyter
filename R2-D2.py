# imports and extensions
import discord
import discord.utils
from discord.ext import commands
from discord.ui import Button, View
data = None
counter = 0
# opening token from token.txt
with open('token3.txt') as file:
    token = file.readlines()

# bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="bot!", intents=intents)
#bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'{bot.user} is now ready!')
    try:
        synced =await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
        status = discord.CustomActivity("Beep Boop")
        await bot.change_presence(status=discord.Status.online, activity=status)
        print(f"Status set to: {status}")
    except Exception as e:
        print(e)

@bot.tree.command(name="countbutton",description="Have fun clicking :D")
async def countbutton(interaction:discord.Interaction):
            global button
            button_view = View()
            button = Button(style=discord.ButtonStyle.blurple, label="1")
            button_view.add_item(button)
            button.callback = lambda j: button_callback(j)

                        # adding the button to the "buttons-collection" (= view)
            await interaction.response.send_message(view=button_view)
            
async def button_callback(interaction: discord.Interaction):
     new_button_view = View()
     new_button = button(label="2")
     new_button_view.add_item(new_button)
     await interaction.response.send_message(view=new_button_view)

# running the bot
bot.run(token[0])