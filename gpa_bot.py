import os
import random
import discord
from discord import Color
from discord.ext import commands
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=['Say ', 'Say', 'say', 'say '])
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    brooklyn_99_quotes = [
        'Senkottu ve saranam etirthaal marnam',
    ]
    if message.content == 'Senkottu':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


@bot.command(name='Gn')
async def nine_nine(ctx):
    await ctx.send('Good night')

@bot.command(name='akshatha_is_cute st')
async def saygm(ctx):
    await ctx.send('Ishtathukku Solla mudiyaathu poda')


@bot.command(name='Gpa')
async def saygpa(ctx,regno="null"):
    status = False
    print(regno)
    try:
        f = open('details.json','r')
        data = json.load(f)
        for details in data:
          if (details['field2']==regno):
              status = True
              sem1_gpa = details['field4']
              sem2_gpa = details['field5']
              sem2_cgpa = details['field6']
              sem3_gpa = details['field7']
              sem3_cgpa = details['field8']
              sem4_gpa = details['field9']
              sem4_cgpa = details['field10']
              sem5_gpa = details['field11']
              sem5_cgpa = details['field12']
              break
          else:
              status = False

        f.close()
    except Exception:
        status = False
    message = discord.Embed(
        title="Gpa/Cgpa Of 5 Semesters",
        description="",
        color=Color.teal(),
    )
    if (regno == "null"):
        message.add_field(name="Reg no", value="Please Enter your Reg no")
        await ctx.send(embed=message)
    elif(status):
        message.add_field(name="Semester 1", value=sem1_gpa)
        message.add_field(name="Semester 2", value=sem2_gpa)
        message.add_field(name="Semester 2 Cgpa", value=sem2_cgpa)
        message.add_field(name="Semester 3", value=sem3_gpa)
        message.add_field(name="Semester 3 Cgpa", value=sem3_cgpa)
        message.add_field(name="Semester 4", value=sem4_gpa)
        message.add_field(name="Semester 4 Cgpa", value=sem4_cgpa)
        message.add_field(name="Semester 5", value=sem5_gpa)
        message.add_field(name="Semester 5 Cgpa", value=sem5_cgpa)
        await ctx.send(embed=message)
    else:
        message.add_field(name="Reg No", value="Register No you have entered Not found")
        await ctx.send(embed=message)

@bot.command(name='gpa')
async def saygpa(ctx,regno="null"):
    status = False
    print(regno)
    try:
        f = open('details.json','r')
        data = json.load(f)
        for details in data:
          if (details['field2']==regno):
              status = True
              sem1_gpa = details['field4']
              sem2_gpa = details['field5']
              sem2_cgpa = details['field6']
              sem3_gpa = details['field7']
              sem3_cgpa = details['field8']
              sem4_gpa = details['field9']
              sem4_cgpa = details['field10']
              sem5_gpa = details['field11']
              sem5_cgpa = details['field12']
              break
          else:
              status = False

        f.close()
    except Exception:
        status = False
    message = discord.Embed(
        title="Gpa/Cgpa Of 5 Semesters",
        description="",
        color=Color.teal(),
    )
    if (regno == "null"):
        message.add_field(name="Reg no", value="Please Enter your Reg no")
        await ctx.send(embed=message)
    elif(status):
        message.add_field(name="Semester 1", value=sem1_gpa)
        message.add_field(name="Semester 2", value=sem2_gpa)
        message.add_field(name="Semester 2 Cgpa", value=sem2_cgpa)
        message.add_field(name="Semester 3", value=sem3_gpa)
        message.add_field(name="Semester 3 Cgpa", value=sem3_cgpa)
        message.add_field(name="Semester 4", value=sem4_gpa)
        message.add_field(name="Semester 4 Cgpa", value=sem4_cgpa)
        message.add_field(name="Semester 5", value=sem5_gpa)
        message.add_field(name="Semester 5 Cgpa", value=sem5_cgpa)
        await ctx.send(embed=message)
    else:
        message.add_field(name="Reg No", value="Register No you have entered Not found")
        await ctx.send(embed=message)


@bot.command(name="about")
async def embed(ctx):
    message = discord.Embed(
        title="Gpa/Cgpa Teller",
        description="Help people to view Their Gpa",
        color=ctx.author.color,
    )

    message.add_field(name="To know briefly about something",
                      value='Use: Say Gpa/gpa RegNo ', inline=False)
    await ctx.send(embed=message)
    print(f"displayed About\n")


bot.run(TOKEN)
