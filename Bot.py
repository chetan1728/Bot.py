import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    
    
@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "<user id>": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission")
    if message.content.upper().startswith('!AMIADMIN'):
        if "<role id>" in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
              
              
  client.run(os.getenv('Token'))            
