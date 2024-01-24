import asyncio
import datetime
import json

import discord
import discord.utils

from discord.ext import commands
from urllib.request import urlopen
import pytz
import requests
from icalendar import Calendar
from datetime import datetime

llmModel = "llama2-uncensored"

question = "Warum sind Bananen krumm"

with open('token.txt') as file:
    token = file.readlines()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="bot!", intents=intents)
bot.remove_command("help")

@bot.command()
async def question(ctx, *args):
    answer = ""
    questionModel = json.dumps({
            "model" : llmModel.lower(), # Das LLM Modell, was genutzt werden soll
            "prompt": ' '.join(args),# Der Prompt vom User
            "stream": True              # Ob es als Stream ausgegeben werden soll (Einfach auf True lassen)
        })
    async with ctx.typing():
    
    # Code von Leo und Pascal angepasst
        with requests.post(url="http://127.0.0.1:11434/api/generate" , data=questionModel, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    answer += json.loads(line)["response"]
                    await asyncio.sleep(2)
    await ctx.send(answer)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def embed(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
    
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = datetime(2023, 12, 20)
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

    


bot.run(token[0])