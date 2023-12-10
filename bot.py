from asyncio import sleep
from audioop import reverse
import time
import discord

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

@client.event
async def on_message(message):
    if message.content.startswith('Hallo'):
        await message.channel.send('Hey, wie geht es dir?')
    elif message.content.startswith('Gut'):
        await message.channel.send('Freut mich!')

@client.event
async def on_message(message):
    if message.content.startswith('Countdown'):
        await message.channel.send('Counting down from 5')
        arr = range(4)
        res = arr[::-1]
        for x in res:
            time.sleep(1)
            await message.channel.send(x+1)        
        await message.channel.send('Wie geht es dir <@302056743066796033>?')
client.run(token[0])




