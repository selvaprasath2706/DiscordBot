import os
import random
import discord
from discord import Color
from discord.ext import commands
from dotenv import load_dotenv
import json
import pandas as pd
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
        'HI Welcome',
    ]
    if message.content == 'Senkottu':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


@bot.command(name='Gn')
async def nine_nine(ctx):
    await ctx.send('Good night')

@bot.command(name="gpaupdate")
async def gpaupdate(ctx):
    sheet_id = "1ZFuspycx3a3b_ds1m4uQm73hfEkZroleCORhxBNxH9c"
    sheet_name = "Sheet1"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    pf = pd.read_csv(url)
    # print(pf)
    pf.to_json(r'details.json')
    await ctx.send(f"Gpa Updated")


@bot.command(name='Gpa')
async def saygpa(ctx,regno="null"):
    status = False
    print(regno)
    try:
        with open('details.json', 'r') as f:
            data = json.load(f)
            namedata = data['REG No. ']
            for i in range(len(namedata)):
                if (str(namedata[str(i)]) == regno):
                    status = True
                    print(data['NAMES '][str(i)])
                    sem1_gpa = data['SEM I GPA'][str(i)]
                    sem2_gpa = data['SEM II GPA'][str(i)]
                    sem3_gpa = data['SEM III GPA'][str(i)]
                    sem4_gpa = data['SEM IV GPA'][str(i)]
                    sem5_gpa = data['SEM V GPA'][str(i)]
                    cgpa = data['CGPA.3'][str(i)]
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
        message.add_field(name="Reg no", value=regno)
        message.add_field(name="Semester 1", value=sem1_gpa)
        message.add_field(name="Semester 2", value=sem2_gpa)
        message.add_field(name="Semester 3", value=sem3_gpa)
        message.add_field(name="Semester 4", value=sem4_gpa)
        message.add_field(name="Semester 5", value=sem5_gpa)
        message.add_field(name="Cgpa", value=cgpa)
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
