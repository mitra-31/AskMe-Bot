import discord
import os
import requests
import json
import questions

"""create instance of client connection for discord"""

client = discord.Client()



@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  """lst = ["$hello","$hi"]"""
  if message.content.startswith("$hello"):
    await message.channel.send("hello")
  elif message.content.startswith("$code"):
    questions(lst,totalLines)

client.run(os.getenv('Token'))
