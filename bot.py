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

client.run(token[0])




