import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from itertools import cycle
import random

print ("Discord Version:", discord.__version__)
version = ("v1.1.0")
print (version)

memberCount= 20       #server info command data
teamCount= 4

Client = discord.Client()                             #setup stuff
client = commands.Bot(command_prefix = "/")    #prefix

suggestions = ("458357907256246292")
report = ("458358536838184982")
botColour = 0xff0000
serverpp = "https://cdn.discordapp.com/attachments/418105976236015622/444183856669655050/EU_CLAN_NEW_LOGO_RED.png"   #data for embed
LFT = "458392331914182666"
tournament = False
#sets game to /help
@client.event
async def on_ready():
    print("\n Ready")
    await client.change_presence(game=discord.Game(name="Use /help"))

        
@client.event
async def on_message(message):
    if message.channel.id == "409451785443475456" and message.author.id == "159985870458322944":
        inaction = True
        asyncio.sleep(3600)
        await client.delete_message(message)
        inaction = False
        

@client.event
async def on_message(message):
    if message.channel.id == "409451785443475456" and message.author.id == "159985870458322944":
        if inaction == True:
            inaction2 = True
            asyncio.sleep(3600)
            await client.delete_message(message)
            inaction2 = False

@client.event
async def on_message(message):
    if message.channel.id == "409451785443475456" and message.author.id == "159985870458322944":
        if inaction == True and inaction2 == True:
            asyncio.sleep(3600)
            await client.delete_message(message)

 
#greets new members with priv msg
@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome!", description=str.title(member.name) + " we hope you enjoy your time at **ExpectUs**, if you need any help feel free to use '/help' or ask an admin", colour=botColour)
    embed.set_thumbnail(url=serverpp)
    embed.set_footer(text=version)
    embed.set_image(url="https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif")
    await client.send_message(member, embed=embed)

        


@client.event                            #all manual commands here
async def on_message(message):
    user = message.author.id
    userName = message.author
    mention = "<@" + user + ">"
    try:
        
     #   member = discord.Server.get_member(user)
        me = await client.get_user_info(user)
        #/info gives server information
        if message.content.upper().startswith('/INFO') or message.content.upper().startswith('/INFOMATION'):
            embed = discord.Embed(title=" ", description="", colour=botColour)
            embed.set_footer(text=version)
            embed.set_thumbnail(url=serverpp)
            embed.add_field(name="Members", value=memberCount, inline=True)
            embed.add_field(name="Teams", value=teamCount, inline=True)
            embed.add_field(name="Leader", value="ReaZy")
            embed.add_field(name="Established", value="11th March 2016", inline=True)
            embed.add_field(name="Games", value="Rocket League\nFortnite")
            await client.send_message(message.channel, embed=embed)
            

         #/steam sends steam link in pm
        if message.content.upper().startswith("/STEAM"):
            embed = discord.Embed(title="Steam", description="Here's the ExpectUs **Steam Group** https://steamcommunity.com/groups/ExpectUSGaming", colour=botColour)
            embed.set_footer(text=version)
            embed.set_thumbnail(url=serverpp)
            await client.send_message(me, embed=embed)
            await client.delete_message(message)
            
        #youtube sends yt link in pm
        if message.content.upper().startswith("/YOUTUBE") or message.content.upper().startswith("/YT"):
            embed = discord.Embed(title="Youtube", description="Here's the ExpectUs **Youtube Channel** https://www.youtube.com/channel/UCSyxTL9PsYWRtwoT6UW095g", colour=botColour)
            embed.set_footer(text=version)
            embed.set_thumbnail(url=serverpp)
            await client.send_message(me, embed=embed)
            await client.delete_message(message)

        if message.content.upper().startswith("/LFT") or message.content.upper().startswith("/LOOKINGFORTEAM"):
            embed = discord.Embed(title=" ", description=" ", colour=botColour)
            embed.set_author(name="How to join ExpectUs")
            embed.add_field(name="-", value="Requesting to join **ExpectUs** is super easy, all you need to do is fill out the sign up form found **below**. Once filled out, an admin will contact you within 3 days at which point you may have an interview and play with team members. Finally we will decide whether to accept you into **ExpectUs** or not.\n\nhttps://goo.gl/forms/y0ApB3MKX80L4EAk1")
            embed.set_thumbnail(url=serverpp)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)

        #suggest things to admin
        if message.content.upper().startswith("/SUGGEST") or message.content.upper().startswith("/SUGGESTION") :
            msg = message.content.split(" ")
            if len(msg) > 4:
                embed = discord.Embed(title="Suggestion", description= (" ".join(msg[1:])), colour=botColour)
                embed.add_field(name="Made by", value=mention)
                embed.set_footer(text=version)
                embed.set_thumbnail(url=serverpp)
                await client.send_message(client.get_channel(suggestions), embed=embed)
                await client.delete_message(message)
                await client.send_message(message.channel, "**Thank you** for the suggestion :wink:")
            else:
                await client.send_message(message.channel, "Suggestion too short")

         #reports a player to admins
        if message.content.upper().startswith("/REPORT"):
            msg = message.content.split(" ")
            if len(msg) > 5:
                embed = discord.Embed(title="Report", description= (" ".join(msg[1:])), colour=botColour)
                embed.add_field(name="Made by", value= message.author, inline=True)
                embed.add_field(name="Person Reported", value= message.mentions[0].mention, inline=True)
                embed.set_footer(text=version)
                embed.set_thumbnail(url=serverpp)
                await client.send_message(client.get_channel(report), embed=embed)
                await client.delete_message(message)
                await client.send_message(message.channel, "Report sent.:hammer:")
            else:
                await client.send_message(message.channel, "Reason too short, add more detail.")
            
        #/twitter sends twitter link in pm
        if message.content.upper().startswith("/TWITTER"):
            embed = discord.Embed(title="Twitter", description="Here's the ExpectUs **Twitter** https://twitter.com/ExpectUs18", colour=botColour)
            embed.set_footer(text=version)
            embed.set_thumbnail(url=serverpp)
            await client.send_message(me, embed=embed)
            await client.delete_message(message)
            
            #/help gives all commands and a description
        if message.content.upper().startswith("/HELP"):
            embed = discord.Embed(title=" ", description=" ", colour=botColour)
            embed.set_author(name="Commands")
            embed.set_thumbnail(url=serverpp)
            embed.set_footer(text= version)
            embed.add_field(name="**/info**", value="Use to find infomation about ExpectUs.")
            embed.add_field(name="**/report <@User>  <reason>**", value="Use to report someone if they break ExpectUs Rules.")
            embed.add_field(name="**/steam**", value="Use to find the Official ExpectUs Steam group.")
            embed.add_field(name="**/youtube**", value="Use to find the Official ExpectUs Youtube channel.")
            embed.add_field(name="**/twitter**", value="Use to find the Official ExpectUs Twitter.")
            embed.add_field(name="**/suggest <suggestion>**", value="Use this to make suggestions on how we could improve ExpectUs and this discord.")       
            await client.send_message(me, embed=embed)
            await client.delete_message(message)
    except:
        await client.send_message(message.channel, "{} use '/help' to see all valid commands.".format(mention))



    
        
        
        
        
        

client.run("NDU3OTc4Mjk0NTYyNzE3Njk3.DghDhg.mUSLaVRhedFbWSRH0Uh1nrJaYF0")  #starts the bot
