from asyncio import sleep
from audioop import reverse
import time
import discord
import random

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
    if (message.content.startswith('Hallo') or message.content.startswith('hallo')):
        userid = message.author.id
        string = '<@' + str(userid) + '>'
        await message.channel.send('Hey, ' + string)
    elif(message.content.startswith('greeting')):
        await message.channel.send('Counting down from 5')
        arr = range(4)
        res = arr[::-1]
        for x in res:
            time.sleep(1)
            await message.channel.send(x+1)        
        await message.channel.send('Hallo <@495912448050593794>?')
    elif(message.content.startswith('joke')):

        joke = ['Egal, wie gut du fährst, Züge fahren Güter.','Wollte Spiderman anrufen – aber der hatte kein Netz.','Wenn sich Wissenschaftler ein Brot belegt, ist es dann wissenschaftlich belegt?','Was machen Mathematiker im Garten? – Wurzeln ziehen','Steht ein Baum allein im Wald.','Übrigens: ich habe gerade ein Blatt gelocht… Aber das nur am Rande.','Was versteht man unter einer Turbine? Nichts – ist viel zu laut!']
        await message.channel.send(random.choice(joke))
        

client.run(token[0])




