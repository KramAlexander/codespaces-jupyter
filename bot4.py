# imports and extensions
import discord.utils
import pytz
import requests
from icalendar import Calendar
from datetime import date, datetime, timedelta
import discord
from discord import app_commands
from discord.ext import commands

# bot declaration
bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())
# opening token from token.txt
with open('token.txt') as file:
    token = file.readlines()

data = None


# start-message of bot
@bot.event
async def on_ready():
    print("Bot is up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="lecture")
async def lecture(interaction: discord.Interaction):
    channel = bot.get_channel(1184076609779671111)
    global data
    global data2
    data = interaction
    view =SimpleView()
    await channel.send(view=view)
    

# creating the buttons
class SimpleView(discord.ui.View):  
      # button for yesterday's lecture plan
      @discord.ui.button(label="Yesterday",style=discord.ButtonStyle.blurple)
      async def hello1(self,interaction:discord.Interaction,button: discord.ui.Button):
             date_entry=date.today() - timedelta(days=1)
             await lecture_data(date_entry)
             await interaction.response.defer()
      # button for today's lecture plan
      @discord.ui.button(label="Today",style=discord.ButtonStyle.green)
      async def hello2(self,interaction:discord.Interaction,button: discord.ui.Button):
             date_entry=date.today()
             await interaction.response.defer()
             await lecture_data(date_entry)           
      # button for tomorrow's lecture plan
      @discord.ui.button(label="Tomorrow",style=discord.ButtonStyle.blurple)
      async def hello3(self,interaction:discord.Interaction,button: discord.ui.Button):
             date_entry=date.today() + timedelta(days=1)
             
             await interaction.response.send_message(await lecture_data(date_entry))


# method called by buttonsclass
async def lecture_data(date_entry):
    global data
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = date_entry #style 2023, 12, 20
    response = requests.get(cal_url)
    if response.status_code == 200:
                # Parse the iCal data
                cal_data = response.text
                # Parse the iCal data using the icalendar library
                cal = Calendar.from_ical(cal_data)
                
                # Extract and print events
                target_date_events = []
                for event in cal.walk('VEVENT'):
                        start_time = event.get('dtstart').dt
                        if start_time.date() == target_date:
                            summary = event.get('summary')
                            end_time = event.get('dtend').dt
                        
                            # Converting UTC+0 to UTC+1
                            target_timezone = pytz.timezone('Europe/Paris')  # Replace with your target timezone
                            start_time = start_time.astimezone(target_timezone)
                            end_time = end_time.astimezone(target_timezone)
                            target_date_events.append({
                                'summary': summary,
                                'start_time': start_time.strftime("%H:%M" + ' Uhr'),
                                'end_time': end_time.strftime("%H:%M" + ' Uhr')
                            })
    # printing out all lectures for the fitting date through discord-embeds
    for event in (target_date_events):
                            channel = bot.get_channel(1184076609779671111)
                            embed = discord.Embed(
                                 
                            title=event['summary'],
                            #description=date,
                            color=discord.Color.blue()  # You can set the color of the embed
                            )
                            # Add fields to the embed
                            embed.add_field(name='Beginn', value=event['start_time'], inline=False)
                            embed.add_field(name='Ende', value=event['end_time'], inline=True)
                    
                            print(f"Summary: {event['summary']}")
                            print(f"Start Time: {event['start_time']}")
                            print(f"End Time: {event['end_time']}")
                            print("-----")
                            await channel.send(embed=embed)

# running bot with token
bot.run(token[0])