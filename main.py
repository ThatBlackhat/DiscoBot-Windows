# blackhat's discord bot start - py
# ----------------------------
# start imports
import discord
from dotenvy import load_env, read_file # fix for windows being lame
from os import environ
import requests
import json

# Load env because windows is retarded and doesn't like os.getenv because its lame
load_env(read_file('.env'))

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} has arrived, ready for duty!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('received')

client.run(environ.get('TOKEN'))