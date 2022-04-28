import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'OTY5MDMwODI5MTEwMDkxODE2.YmneSQ.kmSy1QbdPNz9eNZlxnT82DbemHk'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)