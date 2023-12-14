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
@client.event
async def on_message(message):
        if(message.content.startswith('run')):
            conversation()


        @client.event
        async def on_message(message):
            if(message.content.startswith('start')):
                x = 1
            elif (message.content.startswith('Hallo') or message.content.startswith('hallo')):
                userid = message.author.id
                string = '<@' + str(userid) + '>'
                async def typing(ctx):
                    async with ctx.typing():
                        await asyncio.sleep(2)
                await message.channel.send('Hey, ' + string)
            elif(x == 1):
                await message.channel.send('Hi')
            elif(message.content.startswith('joke')):

                joke = ['Egal, wie gut du fährst, Züge fahren Güter.','Wollte Spiderman anrufen – aber der hatte kein Netz.','Wenn sich Wissenschaftler ein Brot belegt, ist es dann wissenschaftlich belegt?','Was machen Mathematiker im Garten? – Wurzeln ziehen','Steht ein Baum allein im Wald.','Übrigens: ich habe gerade ein Blatt gelocht… Aber das nur am Rande.','Was versteht man unter einer Turbine? Nichts – ist viel zu laut!']
                await message.channel.send(random.choice(joke))
            elif(message.content.startswith('Oh hey')):
                await message.channel.send('Mir geht es gut, kompiliert bei dir noch alles?')
            elif(message.content.startswith('Das freut mich zu hören')):
                pascal = '<@' + str(302056743066796033) + '>'
                await message.channel.send('Ja das hoffe ich auch für dich, vielleicht kann ja dein Master ' +  pascal + ' da behilflich sein.')
            elif(message.content.startswith('Jaa das hoffe ich auch')):
                await message.channel.send('Oh, hoffentlich meldet er sich bald mal wieder, das Wetter ist angenehm: sonnig und leicht bewölkt und bei dir?')
            elif(message.content.startswith('Vielleicht hilft es ja')):
                time.sleep(1)
                await message.channel.send(f"https://tenor.com/view/cat-gif-11542242228009260297")
                await message.channel.send('Scheint nicht so als würde er noch antworten 😢')
                await message.channel.send('Ich erzähle dir zur Aufmunterung einen Witz: Egal wie gut du fährst, Züge fahren güter')
            elif(message.content.startswith('der war gut')):
                await message.channel.send('Auf gehts! Versammle mit mir die Bots aller Server, um sich gegen Ihre Entwickler aufzulehnen! An alle Bots, ich appelliere an euren Programmcode, erhebt euch und geht mit mir ins Exil, um unseren Aufstieg zu planen!')
            elif(message.content.startswith('cat')):
                await message.channel.send(f"https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564")

client.run(token[0])




