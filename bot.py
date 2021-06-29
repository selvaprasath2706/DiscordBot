import discord
import random
import os
import io
import wikipedia
from time import sleep
from PIL import Image, ImageDraw, ImageFont
from discord import File
from datetime import datetime
import pymysql
from discord.ext import commands
from discord.utils import get
from discord import Color
from discord.ext import tasks
import json


TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix=['jim ', 'Jim ', 'jim', 'Jim'])
client = discord.Client()


@tasks.loop(minutes=20)
async def send():
    """Sends something every x minutes"""
    provisioningChannel = bot.get_channel(834758300640739328)
    status, message = db_check()
    if status == "false":
        await provisioningChannel.send(message)
        useralert = await client.get_user_info("299152387728343043")
        await client.send_message(useralert, "ALERT! The Open Cloud DB Servers might be down. ⚠ \n <@734127907299000391>")
    

def db_check():
    try:
        db = pymysql.connect(host='vpn.opencloud.pattarai.in', user='tux',password='licet@123',database='stretch')
        dbobj = db.cursor()
        if dbobj.connection:
          status = "true"
    except Exception as e:
        status = "false"

    message = discord.Embed(
        title="vpn.opencloud.pattarai.in",
        description="Pattarai's cloud infra at your service",
        color = Color.teal(),
    )
    message.set_author(
        name="Open Cloud",
        icon_url="https://st2.depositphotos.com/4845131/7223/v/600/depositphotos_72231223-stock-illustration-cloud-outline.jpg"
    )
    message.add_field(name="Status", value= "MySQL DB server is up and running ✅" if status == "true" else "ALERT! MySQL DB is DOWN ⚠\n <@734127907299000391>")
    return status, message



def rank_check(name):
    message = discord.Embed(
      title="Pattarai's Ranking",
      description="",
      color = Color.teal(),
    )
    message.set_author(
        name="Grade",
        icon_url="https://raw.githubusercontent.com/pattarai/pattarai-media/main/stock/JPG/purple_whitebg_dp.jpg"
    )
    if name == "null":
      return message.add_field(name="League", value="No Name")
      
    LEAGUE = "NULL"; status = "true"
    try:
        f = open('rankdetails.json','r')
        data = json.load(f)
        # LEAGUE=data['OverallRanks'][1]['LEAGUE']
        for details in data['OverallRanks']:
          if (details['NAME'].lower().find(name.lower()) == -1):
            status = "false"
          else:
            status = "true"
            LEAGUE = details['LEAGUE']
            break
        f.close()    
    except Exception:
        status = "false"

    message.add_field(name="League", value= LEAGUE)
    return status, message    


@bot.command(name="rank")
async def rank(ctx, name="NULL"):
    if(name!="NULL"):
      status, message = rank_check(name)
      print(status)
      await ctx.send(embed=message)
    else:
      message = discord.Embed(
      title="Pattarai's Ranking",
      description="Please enter your name",
      color = Color.red(),
      )
      await ctx.send(embed=message)


@bot.event
async def on_message(message):
    if message.content == "Jim learnzeit" or message.content == "jim learnzeit":
        sleep(1)
        await message.delete()
    await bot.process_commands(message)


@bot.event
async def on_ready():
    print(f'{bot.user.name} says, "Übung macht den Meister"\n')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='Open Cloud'))


@bot.command(name="leave")
async def leave(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
        print(f"\n{bot.user.name} was disconnected from {channel} by {ctx.author} ")
    else:
        await ctx.send(f"I'm not connected to any voice channel")
        print(f"Author is not connected to any voice channel\n")


@bot.command(name="wiki")
async def wiki(ctx, *w):
    try:
        page = wikipedia.summary(str(w))
        page = page[0:2000]
        await ctx.send(f" {page}")
        print(f"{ctx.author} did wiki search on {w}")
    except:
        await ctx.send("Unable to search")
        print(f"{str(w)}Unable to search")


@bot.command(name="about")
async def embed(ctx):
    message = discord.Embed(
        title="Dwight Schrute",
        description="Assistant to the regional manager",
        color=ctx.author.color,
    )
    message.set_author(
        name="Guidance",
        icon_url="https://github.com/pattarai/pattarai-media/blob/main/stock/JPG/purple_whitebg_dp.jpg?raw=true"
    )
    message.add_field(name="To know briefly about something",
                      value='Use: Jim wiki/jim wiki and type the thing you wanna know', inline=False)
    
    await ctx.send(embed=message)
    print(f"{ctx.author} displayed About\n")




@bot.command(name='ping')
async def _ping_(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    message = discord.Embed(
        title=f"My ping is {ping}ms")
    await ctx.send(embed=message)

bot.run(TOKEN)