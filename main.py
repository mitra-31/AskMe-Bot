import discord
import os
import requests
import json, random
from app import questions




"""create instance of client connection for discord"""

client = discord.Client()


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #Greeting Reply
    if message.content.startswith("$hello"):
        await message.channel.send("hello")

    #Coding Question Reply
    elif message.content.startswith("$code"):
        lst = questions.lst
        #print(lst)
        questions_list = []
        lineCount = 0
        for row in lst:
          if lineCount == 0:
            lineCount += 1
            continue
          else:
           # print(row[0])
            questions_ = row[0].split(",")
            questions_list.append(questions_)
        print(questions_list)
        #print(len(questions_list))
        r = random.randint(0, len(questions_list)-1)
        #print(r)
        css = "Topic : {0}\nProblem : {1}\nLink : {2}".format(questions_list[r][0], questions_list[r][1],questions.link(questions_list[r][1]))
        await message.channel.send(css)


client.run(os.getenv('Token'))
