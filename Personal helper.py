import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import time
import random
import aiohttp
import json
import requests
from discord import Game



BOT_PREFIX = ("?", "!")
Client = discord.client
client = Bot(command_prefix=BOT_PREFIX)
Clientdiscord = discord.Client()
DESCRIPTION = "Discord bot running on Python!"
#bot = commands.Bot(command_prefix="?", description=DESCRIPTION)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='With your brain'))
    print('Ready')

     
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='Hello',
                #description="Answers a yes/no question.",
                brief="Bot and you hello ease other",
                aliases=['hello', 'hlw', 'hi','Hi'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'HI DEAR',
        'Hi dear',
        'HELLO DEAR',
        'Hello dear',
        'Hi',
        'HI',
        'HELLO',
        'Hello',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    
@client.command(name='Fuck',
                #description="Answers a yes/no question.",
                brief="Try it yourself and see haha.",
                aliases=['Ahfuck','ahfuck','fuck','ahhfuck'],
                pass_context=True)
async def Ahfuck(context):
    possible_responses = [
        'YOU',
        'Bad boy huh !',
        'Go and fuck your GF',
        'You',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


    
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
    
@client.command()
async def BTC():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
        
@client.command(pass_context=True)
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.User=None):
    """ Simple ban command """
    await client.ban(member)
    print("banned" + " " + str(member))

if __name__ == '__main__':
    print('we are in main!')
    
@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.User=None):
    """ Simple kick command """
    await client.kick(member)
    print("kicked" + " " + str(member))
    await client.say("KICKED...........")

client.run(os.gatenv('TOKEN;'))
