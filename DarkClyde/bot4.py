# imports and extensions
import discord.utils
import pytz
import requests
from icalendar import Calendar
from datetime import date, datetime, timedelta
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

# bot declaration
bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())
# opening token from token.txt
with open('token.txt') as file:
    token = file.readlines()

data = None
counter = 0

#start-message of bot
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
    await interaction.response.send_message(view=view)
    
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
             try:
                await interaction.response.send_message(await lecture_data(date_entry))
             except:
                    print("error")
# method called by buttonsclass
async def lecture_data(date_entry):
    print("erreicht")
    global data
    cal_url = "https://stuv.app/MOS-TINF23A/ical"
    target_date = date_entry #style 2023, 12, 20
    print(date_entry)
    print(type(date_entry))
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
                       
                        #print(start_time)
                        #print(target_date)
                        if start_time.date() == target_date:
                            summary = event.get('summary')
                            end_time = event.get('dtend').dt
                            room = event.get('location')
                            print("x")
                            if (len(room)==22):
                                   room = room[:7]
                            elif(len(room)==23):
                                   room = room[:8]
                            elif(len(room)==25):
                                   room = room[:10]
                                   
                            # Converting UTC+0 to UTC+1
                            target_timezone = pytz.timezone('Europe/Paris')  # Replace with your target timezone
                            start_time = start_time.astimezone(target_timezone)
                            end_time = end_time.astimezone(target_timezone)
                            target_date_events.append({
                                'summary': summary,
                                'start_time': start_time.strftime("%H:%M" + ' Uhr'),
                                'end_time': end_time.strftime("%H:%M" + ' Uhr'),
                                'room': room
                            })                           
    # printing out all lectures for the fitting date through discord-embeds
    for event in (target_date_events):
                            channel = bot.get_channel(1184076609779671111)
                            embed = discord.Embed(
                            title = "**"+str(event['summary'])+"**",
                            #description=date,
                            color=discord.Color.blurple()  # You can set the color of the embed
                            )
                            # Add fields to the embed
                            embed.add_field(name='__Beginn:__', value=event['start_time'], inline=False)
                            embed.add_field(name='__Ende:__', value=event['end_time'], inline=True)
                            embed.add_field(name='__Vorlesungsort:__', value=event['room'], inline=False)
                            embed.set_image(url="https://cdn.discordapp.com/attachments/909054108235862066/1197594048781893694/541px-DHBW-Logo.png?ex=65bbd55f&is=65a9605f&hm=8d57652450766fa4a11d1dc6ff195858d72c83b76dda26e898e8a59d1b8606a1&")
                            
                            print(f"Summary: {event['summary']}")
                            print(f"Start Time: {event['start_time']}")
                            print(f"End Time: {event['end_time']}")
                            print(f"Room: {event['room']}")
                            print("-----")
                            await channel.send(embed=embed)

def jan1():
  year = datetime.today().strftime("%Y")
  jan1 = datetime(int(year), 1, 1, 0, 0, 0, 0).weekday()
  return jan1

@bot.tree.command(name="buttontest")
async def lecture(interaction: discord.ui.Button):
    channel = bot.get_channel(1184076609779671111)
    global data
    global data2
    data = interaction
    view = await buttons(interaction)
    await interaction.response.send_message(view=view)

async def buttons(interaction: discord.Interaction):
       global data
       data = interaction
       for i in range(0,6):
              if jan1() == 0:
               year = datetime.today().strftime("%Y")
               firstmonday = datetime(int(year), 1, 1, 12, 0, 0, 0) + timedelta(days=i)
              else:
               firstmonday = datetime(int(year), 1, 1, 12, 0, 0, 0) + timedelta(days=7-i)
              view = View()

              async def callback1(interaction):             
               global counter
               counter = counter + 1
               print(counter)
               startmonday = firstmonday+timedelta(days=7*counter)
               print(startmonday)
               view2 =View()              
               for j in range(0,5):
                     if j % 2 !=0:
                            temp = j
                            j = (Button(custom_id = f"{interaction.id}~{startmonday+timedelta(days=temp)}",style=discord.ButtonStyle.green, label=str((startmonday+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view2.add_item(j)
                            j.callback = lambda j: callback2(j)
                     else:
                            temp = j
                            j = (Button(custom_id = f"{interaction.id}~{startmonday+timedelta(days=temp)}",style=discord.ButtonStyle.blurple, label=str((startmonday+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view2.add_item(j)
                            j.callback = lambda j: callback2(j)
              
               button=(Button(style=discord.ButtonStyle.gray,label="Previous",row = 0))
               view2.add_item(button)
               # Button general
               button2=(Button(style=discord.ButtonStyle.gray,label="lecture from January 01 - 05",row=0))
               view2.add_item(button2)
               # Button next
               button3=(Button(style=discord.ButtonStyle.gray,label="Next",row=0))
               view2.add_item(button3)
               button3.callback = callback1
               await interaction.response.edit_message(view=view2)
                         
              # Button previous
              button=(Button(style=discord.ButtonStyle.gray,label="Previous",row = 0))
              view.add_item(button)
              button.callback = callback1
              # Button general
              button2=(Button(style=discord.ButtonStyle.gray,label="lecture from January 01 - 05",row=0))
              view.add_item(button2)
              button2.callback = callback1
              # Button next
              button3=(Button(style=discord.ButtonStyle.gray,label="Next",row=0))
              view.add_item(button3)
              button3.callback = callback1

              async def callback2(interaction: discord.Interaction):
                      #date_entry=date.today()+ timedelta(days=1)####################
                   # try:
                      print(interaction.data)
                      date = interaction.data['custom_id'].split('~')[1]
                      await lecture_data(datetime.strptime(date,"%Y-%m-%d %H:%M:%S").date())
                      await interaction.response.defer()
                      
                    #except Exception as e:
                       #     print(e)
              temp = []
              callback = []
              for j in range(0,5):
                     if j % 2 != 0:
                            temp.append(j)
                            temp2 = j
                            j = (Button(custom_id = f"{interaction.id}~{firstmonday+timedelta(days=temp2)}",style=discord.ButtonStyle.green, label=str((firstmonday+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view.add_item(j)                             
                            j.callback = lambda j: callback2(j)
                            callback.append(j.callback)
                     else:
                            temp2 = j
                            j = (Button(custom_id = f"{interaction.id}~{firstmonday+timedelta(days=temp2)}",style=discord.ButtonStyle.blurple, label=str((firstmonday+timedelta(days=j)).strftime("%d.%m")),row=1))
                            view.add_item(j)
                            j.callback = lambda j: callback2(j)
                            callback.append(j.callback)

                     
              
              #print(callback)
              #print(temp) 
              
              return view
              
       

# running bot with token
bot.run(token[0])