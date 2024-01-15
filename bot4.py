# imports and extensions
import discord.utils
import pytz
import requests
from icalendar import Calendar
from datetime import date, datetime, timedelta
import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())
# opening token from token.txt
with open('token.txt') as file:
    token = file.readlines()

data = None
counter = 0

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
    date_entry=date.today()
    global data
    data = interaction
    await lecture_data(date_entry)




async def lecture_data(date_entry):
    global data
    interaction = data
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = date_entry #style 2023, 12, 20
    response = requests.get(cal_url)
    if response.status_code == 200:
                # Parse the iCal data
                cal_data = response.text
                # Parse the iCal data using the icalendar library
                cal = Calendar.from_ical(cal_data)
                print(cal)
                # Extract and print events
                target_date_events = []
                for event in cal.walk('VEVENT'):
                        start_time = event.get('dtstart').dt
                        if start_time.date() == target_date:
                            summary = event.get('summary')
                            end_time = event.get('dtend').dt
                        
                            # Convert UTC+0 to UTC+1
                            target_timezone = pytz.timezone('Europe/Paris')  # Replace with your target timezone
                            start_time = start_time.astimezone(target_timezone)
                            end_time = end_time.astimezone(target_timezone)
                            target_date_events.append({
                                'summary': summary,
                                'start_time': start_time.strftime("%H:%M" + ' Uhr'),
                                'end_time': end_time.strftime("%H:%M" + ' Uhr')
                            })

    for event in target_date_events:
                            embed = discord.Embed(
            
                            title=event['summary'],
                            #description=date,
                            color=discord.Color.blue()  # You can set the color of the embed
                            )
                            # Add fields to the embed
                            embed.add_field(name='Beginn', value=event['start_time'], inline=False)
                            embed.add_field(name='Ende', value=event['end_time'], inline=True)
                        
                            print(f"Summary: {event['summary']}")
                            #print(f"Start Time: {event['start_time']}")
                            print(f"End Time: {event['end_time']}")
                            print("-----")
                            await interaction.response.send_message(embed=embed)

bot.run(token[0])