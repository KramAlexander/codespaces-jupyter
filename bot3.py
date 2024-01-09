# imports and extensions
import asyncio
import datetime
import discord
import discord.utils
from discord.ext import commands
import pytz
import requests
from icalendar import Calendar
from datetime import datetime

# opening token from token.txt
with open('token.txt') as file:
    token = file.readlines()

# bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="bot!", intents=intents)
bot.remove_command("help")

# Log-In-Confirmation
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# command for getting lecture plan
@bot.command()
async def lecture(ctx,date_entry):
    async with ctx.typing():
        await asyncio.sleep(2)
    year, month, day = map(int, date_entry.split('-'))
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = datetime(year, month, day) #style 2023, 12, 20
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

                    if start_time.date() == target_date.date():
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

            # Print all events for the target date
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
                    await ctx.send(embed=embed)

                        
    else:
                print(f"Failed to retrieve the iCal data. Status code: {response.status_code}")

    

# running bot
bot.run(token[0])