import discord
from discord.ext import commands
import requests
import pathlib
import datetime
import time
import os
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot connected:')
    print('Name: {}'.format(bot.user))
    print('ID: {}'.format(bot.user.id))

@bot.event
async def on_message(message):
    if message.author.bot == False:
        if message.content.startswith in ignored:
            pass
        else:
            if not message.attachments:
                pathlib.Path("./servers/" + str(message.guild.id) + "/").mkdir(parents=True, exist_ok=True)
                pathlib.Path("./servers/" + str(message.guild.id) + "/channels/").mkdir(parents=True, exist_ok=True)
                pathlib.Path("./servers/" + str(message.guild.id) + "/channels/" + "images/").mkdir(parents=True, exist_ok=True)
                chatlog = open("./servers/"+ str(message.guild.id) + "/channels/" + str(message.channel.id) + "-" + str(message.channel.name) + ".txt", "a+")
                t = time.strptime(str(message.created_at), "%Y-%m-%d %H:%M:%S.%f")
                msg12hr = time.strftime( "%b-%d-%Y %I:%M %p", t )
                chatlog.write(str(message.author) + " | Message: " + str(message.content) + " | ID: " + str(message.id) + " | " + str(msg12hr) + " UTC" + "\n")
                info = open("./servers/"+ str(message.guild.id) + "/" "info.txt", "w+")
                info.write("Name: " + str(message.guild.name) + "\nOwner: " + str(message.guild.owner) + "\nMembers: " + str(message.guild.member_count))
            else:
                try:
                    pathlib.Path("./servers/" + str(message.guild.id) + "/").mkdir(parents=True, exist_ok=True)
                    pathlib.Path("./servers/" + str(message.guild.id) + "/channels/").mkdir(parents=True, exist_ok=True)
                    chatlog = open("./servers/" + str(message.guild.id) + "/channels/" + str(message.channel.id) + "-" + str(message.channel.name) + ".txt", "a+")
                    t = time.strptime(str(message.created_at), "%Y-%m-%d %H:%M:%S.%f")
                    msg12hr = time.strftime( "%b-%d-%Y %I:%M %p", t )
                    chatlog.write(str(message.author) + " | Message: " + str(message.content) + " | Image: " + str(message.attachments[0].id) + " | " + str(msg12hr) + " UTC" + "\n")
                    await message.attachments[0].save("./servers/" + str(message.guild.id) + "/channels/images/"+ str(message.attachments[0].id) + ".png")
                except IndexError:
                    pass


client.run(os.getenv('Token'))
