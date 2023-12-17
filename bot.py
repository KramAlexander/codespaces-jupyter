from asyncio import sleep
import asyncio
from audioop import reverse
import time
import discord
import random
from discord.ext import commands


with open('token.txt') as file:
    token = file.readlines()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@commands.command()
async def typing(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
def function():
    print('Hello World')       
function()
@client.event
async def on_message(message):
    if(message.content.startswith('Hallo')):
        await message.channel.send('Hello World')

client.run(token[0])



 if start_time.date() == target_date.date():
                summary = event.get('summary')
                end_time = event.get('dtend').dt
                target_date_events.append({
                'summary': summary,
                'start_time': start_time,
                'end_time': end_time
            })
        for event in target_date_events:         
                summary = event.get('summary')
                start_time = event.get('dtstart').dt 
                starttime = start_time.strftime("%H:%M")
                end_time = event.get('dtend').dt
                endtime = end_time.strftime("%H:%M")
                date = start_time.strftime("%d.%m.%Y")
            
