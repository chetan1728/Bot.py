import discord, asyncio, random, os
from discord.ext.commands import Bot

x = " [ \ 033 [92m * \ 033 [0m] "
y = " [ \ 033 [91m * \ 033 [0m] "

client = Bot ( command_prefix = " $ " )

@ client.event
async  def  on_ready ():
    print (x + client.user.name + " as login. " )
    print (client.user.id)

@ client.command ( pass_context  =  True )
async  def  info ( ctx , * args ):
    await client.delete_message (ctx.message)
    await client.say ( " $ steam -to get the steam community group \ n $ collec -to get the gmod \ n $ site server collection -to get the community site / forum. " )

@ client.command ( pass_context  =  True )
async  def  steam ( ctx , * args ):
    await client.delete_message (ctx.message)
    await client.say ( " http://steamcommunity.com/groups/frontlineroleplaycommunity " )

@ client.command ( pass_context  =  True )
async  def  collec ( ctx , * args ):
    await client.delete_message (ctx.message)
    await client.say ( " http://steamcommunity.com/sharedfiles/filedetails/?id=682392848 " )

@ client.command ( pass_context  =  True )
async  def  site ( ctx , * args ):
    await client.delete_message (ctx.message)
    await client.say ( " http://frontlineroleplaycommunity.phy.sx " )

@ client.event
async  def  on_member_remove ( member ):
    print (y + member.name +  " just left. " )
    await client.send_message (discord.Object ( id = " id channel " ), member.mention + " just quit !:( " )

@ client.event
async  def  on_member_join ( member ):
    print (x + member.name +  " just joined. " )
    await client.send_message (discord.Object ( id = ' id channel ' ), " Welcome to " + member.mention + " on Frontline Roleplay \ n You can watch the channel #DEV to see the advanced server! \ n N do not forget to read the rules! " )
    role = discord.utils.get (member.server.roles, name = " Arriving " )
    await client.add_roles (member, role)
    print (x + " The role "  + role.name +  " was added to "  + member.name)
    
client.run(os.getenv('Token'))
