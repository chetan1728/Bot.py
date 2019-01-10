import discord
from discord.ext import commands
import asyncio
import youtube_dl
#from itertools import cycle

data = open('configure.txt').read().split('\n')
playlist = open('playlist').read().split('\n')

token = data[1]

prefix = data[3]

client = commands.Bot(command_prefix = prefix)

players = {}
queues = {}

#push the next song into player
def check_queue(id):
    print('Check If Enter')
    if queues[id] != []:
        player = queues[id].pop(0)
        print('Check If Player dowland')
        players[id] = player
        print('player')
        player.start()
    else:
        del players[id]


@client.event
async def on_ready():
    #show the presence
    await client.change_presence(game=discord.Game(name='Test'))
    print("Bot online.")

#Join the Bot into your voice channel
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

#leave the Bot into your voice channel
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url=None):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    if server.id not in players:
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        players[server.id] = player
        player.start()
    else:
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        if server.id in queues:
            queues[server.id].append(player)
        else:
            queues[server.id] = [player]
        await client.say('Video queued.')


@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()


@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()


@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

'''#add the url into queues
@client.command(pass_context=True)
async def queue(ctx, url=None):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    if url == None:
        for i in playlist:
            player = await voice_client.create_ytdl_player(i)
            if server.id in queues:
                queues[server.id].append(player)
            else:
                queues[server.id] = [player]
            await client.say('list is queuing.')'''


client.run(token) 
