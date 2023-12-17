import asyncio
import datetime
import time
import discord
import discord
import discord.utils
import asyncio

from discord.ext import commands
from discord import app_commands
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import requests
import icalendar
from icalendar import Calendar
from datetime import datetime
with open('token.txt') as file:
    token = file.readlines()
    


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="bot!", intents=intents)
bot.remove_command("help")


cal_url = "https://stuv.app/MOS-TINF23A/ical"
target_date = datetime(2023, 12, 18)
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

                    target_date_events.append({
                        'summary': summary,
                        'start_time': start_time,
                        'end_time': end_time
                })

        # Print all events for the target date
            for event in target_date_events:
                
                print(f"Summary: {event['summary']}")
                print(f"Start Time: {event['start_time'] }")
                print(f"End Time: {event['end_time']}")
                print("-----")
               
                    
else:
            print(f"Failed to retrieve the iCal data. Status code: {response.status_code}")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

 

@bot.command()
async def embed(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
    embed = discord.Embed(
       
        title=summary,
        #description=date,
        color=discord.Color.blue()  # You can set the color of the embed
    )
    # Add fields to the embed
    embed.add_field(name='Fach', value=event['start_time'], inline=False)
    embed.add_field(name='Beginn', value=event['end_time'], inline=True)

    # Set the footer of the embed
    #embed.set_footer(text = date)

    # Send the embed message to the channel
    await ctx.send(embed=embed)

def data():
    @bot.command()
    async def embed(ctx):
         await ctx.send(embed=embed)

bot.run(token[0])