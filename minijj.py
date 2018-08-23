import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
from itertools import cycle
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

print ("Discord Version:", discord.__version__)
version = ("v1.1.2")
print (version)


memberCount= 20       #server info command data
teamCount= 4

Client = discord.Client()                             #setup stuff
client = commands.Bot(command_prefix = "/")    #prefix

suggestions = ("458357907256246292")
report = ("458358536838184982")
expectusgreenava = "Update"
expectusava = "Update"
expectusfortniteava = "Update"
expectusblueava = "Update"

botColour = 0xff0000
serverpp = "https://cdn.discordapp.com/attachments/418105976236015622/444183856669655050/EU_CLAN_NEW_LOGO_RED.png"   #data for embed
logs = "472540593621434369"
resp = "481971486496784395"

tournament = False
#sets game to /help
@client.event
async def on_ready():
    print("\n Ready")
    await client.change_presence(game=discord.Game(name="Use /help"))
    ready = True
 #   await client.change_presence(game=discord.Game(name="Use /help", url="https://www.twitch.tv/mongraal", type=1))
    await auto_stream()

@client.event
async def on_typing(channel, user, when):
    await responses()
#@client.event
#async def on_ready():

#    await responses()

   
@client.event
async def responses():
    print("Responses: Active")
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("Responses.json", scope)
    client2 = gspread.authorize(creds)
    sheet = client2.open("ExpectUs Responses").sheet1
    loop = True
    lastCount = 100
    x = 2
    try:

        while loop == True:
            await asyncio.sleep(15)
            loop2 = True
            
            
            while loop2 == True:
                await asyncio.sleep(1)
                
                
                if sheet.cell(x, 1).value != "":
                    x = x+1
                else:
                    loop2 = False
            
            responseCount = x-1

            if responseCount > lastCount:
                
                response = sheet.row_values(responseCount)
                user_time = sheet.cell(responseCount ,1).value
                user_email = sheet.cell(responseCount ,2).value
                user_team = sheet.cell(responseCount ,3).value
                user_discord = sheet.cell(responseCount ,4).value
                user_name = sheet.cell(responseCount ,5).value
                user_age = sheet.cell(responseCount ,6).value
                user_country = sheet.cell(responseCount ,7).value
                user_reason = sheet.cell(responseCount ,8).value
                user_rate = sheet.cell(responseCount ,9).value
                user_hours = sheet.cell(responseCount ,11).value

                embed = discord.Embed(title="New Request", description= "", colour=botColour)
                embed.set_thumbnail(url=serverpp)
                embed.set_footer(text=user_time)
                embed.add_field(name= "Discord", value= user_discord)
                embed.add_field(name= "Email", value= user_email)
                embed.add_field(name= "Team to join", value= user_team)
                embed.add_field(name= "Reason", value= user_reason)
                embed.add_field(name= "GamerTag", value= user_name)
                embed.add_field(name= "Age", value= user_age)
                embed.add_field(name= "Rate themselves", value= user_rate)
                embed.add_field(name= "How often play", value= user_hours)
                embed.add_field(name= "Country", value= user_country)

                
                await client.send_message(client.get_channel(resp), embed=embed)
                lastCount = responseCount                 


            else:
                
                lastCount = responseCount
    except:
        await asyncio.sleep(60)
        

@client.event
async def auto_stream():
    print("Auto Stream: Active")
    await asyncio.sleep(60)
    for member in client.get_all_members():
      
        try:
            role = discord.utils.get(member.server.roles, name="Streaming")
            game = str(member.game)
            streaming = discord.utils.get(member.roles, name="Streaming")
            if game == "None":
                await client.remove_roles(member, role)                          
            else:
                if member.game.type == 1:
                    if streaming == "Streaming":
                        streamrole = True
                    else:
                        await client.add_roles(member, role)                        
                else:
                    await client.remove_roles(member, role)
        except:
            await auto_stream()

@client.event
async def on_message_delete(message):
    if message.author != "Mini-JJ#8780":
        await client.send_message(client.get_channel(logs), " {} deleted - '{}' ".format(message.author, message.content))

@client.event
async def on_member_ban(member):
    await client.send_message(client.get_channel(logs), " {} has benn banned".format(member.name))
    
    
    
            
                
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
 #   serverpp = message.server.icon_url
    user = message.author.id
    userName = message.author
    mention = "<@" + user + ">"
##    try:
    
 #   member = discord.Server.get_member(user)
    me = await client.get_user_info(user)
    #/info gives a players information
    if message.content.upper().startswith("/INFO"):
        member = message.mentions[0]
        embed = discord.Embed(title="{}'s Info".format(member.name), description="", colour=botColour)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Status", value=member.status, inline=True)
        embed.add_field(name="Joined at", value=member.joined_at, inline=True)
        if member.game != "None":
            embed.add_field(name="Game", value=member.game, inline=True)
        if member.nick != "None":
            embed.add_field(name="Nickname", value=member.nick, inline=True)
        embed.add_field(name="Highest role", value=member.top_role, inline=True)
        embed.set_footer(text=version)
        
        msg = await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    
            
             
 



## /ingame to display everyone online in that game
    if message.content.upper().startswith("/INGAME"):
        msg = message.content.split(" ")
        if len(msg) > 1:
            del msg[0]
            ingame = []
            game1 = " ".join(msg)
            if str.upper(game1) == "PUBG":
                game1 = "PLAYERUNKNOWN'S BATTLEGROUNDS"
            elif str.upper(game1) == "CSGO":
                game1 = "Counter-Strike Global Offensive"
            elif str.upper(game1) == "RL":
                game1 = "Rocket League"
            for member in client.get_all_members():             
                game2 = str(member.game)
                if str.upper(game2) == str.upper(game1):
                    ingame.append(member.name)
            if len(ingame) < 1:
                msg = await client.send_message(message.channel, "**No one** is currently playing that game.:rolling_eyes:")
                await asyncio.sleep(0.03)
                client.delete_message(msg)

            else:
                embed = discord.Embed(title="", description="", colour=botColour)
                embed.set_author(name="User(s) playing {}".format(str.title(game1)))
                embed.set_footer(text=version)
                embed.set_thumbnail(url=serverpp)
                embed.add_field(name="In Game", value=len(ingame), inline=False)
                if len(ingame) < 6:
                    embed.add_field(name="User(s)", value="\n".join(ingame), inline=False)
                else:
                    embed.add_field(name="User(s)", value=", ".join(ingame), inline=False)
                
                await client.send_message(message.channel, embed=embed)
                
                                
    if message.content.upper().startswith("/AVA"):
        if "472810916295999520" in [roles.id for roles in message.author.roles]:
            
            if message.content.upper().startswith("/AVA EXPECTUS 1"):
                expectusava = "Full :x:"
            if message.content.upper().startswith("/AVA EXPECTUS 2"):
                expectusava = "Looking for members :white_check_mark:"
            if message.content.upper().startswith("/AVA EXPECTUS 3"):
                expectusava = "Full"
            if message.content.upper().startswith("/AVA EXPECTUS BLUE 1"):
                expectusblueava = "Full :x:"
            if message.content.upper().startswith("/AVA EXPECTUS BLUE 2"):
                expectusblueava = "Looking for members :white_check_mark:"
            if message.content.upper().startswith("/AVA EXPECTUS BLUE 3"):
                expectusblueava = "Full"
            if message.content.upper().startswith("/AVA EXPECTUS GREEN 1"):
                expectusgreenava = "Full :x:"
            if message.content.upper().startswith("/AVA EXPECTUS GREEN 2"):
                expectusgreenava = "Looking for members :white_check_mark:"
            if message.content.upper().startswith("/AVA EXPECTUS GREEN 3"):
                expectusgreenava = "Full"
            if message.content.upper().startswith("/AVA EXPECTUS FORTNITE 1"):
                expectusfortniteava = "Full :x:"
            if message.content.upper().startswith("/AVA EXPECTUS FORTNITE 2"):
                expectusfortniteava = "Looking for members :white_check_mark:"
            if message.content.upper().startswith("/AVA EXPECTUS FORTNITE 3"):
                expectusfortniteava = "Full"

            if message.content.upper().startswith("/AVA START"):
                embed = discord.Embed(title="Team availibilty", description="Before requesting to join a team, check the availibility of that team. If the team is in need of players you are more likely to be accepted.", colour=botColour)
                embed.add_field(name="ExpectUs", value="Update")
                embed.add_field(name="ExpectUs Blue", value="Update")
                embed.add_field(name="ExpectUs Green", value="Update")
                embed.add_field(name="ExpectUs Fortnite", value="Update")

                embed.set_thumbnail(url=serverpp)
                avamsg = await client.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="Team availibilty", description="Before requesting to join a team, check the availibility of that team. If the team is in need of players you are more likely to be accepted.", colour=botColour)
                embed.add_field(name="ExpectUs", value=expectusava)
                embed.add_field(name="ExpectUs Blue", value=expectusblueava)
                embed.add_field(name="ExpectUs Green", value=expectusgreenava)
                embed.add_field(name="ExpectUs Fortnite", value=expectusfortniteava)

                embed.set_thumbnail(url=serverpp)
                await client.edit_message(avamsg, embed=embed)
            
            
                    
                
            
        


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

   #  if message.content.upper().startswith("/LFT"):
#        embed = discord.Embed(title=" ", description=" ", colour=botColour)
#        embed.set_author(name="How to join ExpectUs")
#        embed.add_field(name="-", value="Requesting to join **ExpectUs** is super easy, all you need to do is fill out the sign up form found **below**. Once filled out, an admin will contact you within 3 days at which point you may have an interview and play with team members. Finally we will decide whether to accept you into **ExpectUs** or not.\n\nhttps://goo.gl/forms/y0ApB3MKX80L4EAk1")
#        embed.set_thumbnail(url=serverpp)
#        await client.send_message(message.channel, embed=embed)
#        await client.delete_message(message)

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

    if message.content.upper().startswith("/STORE") or message.content.upper().startswith("/SHOP"):
        embed = discord.Embed(title="ExpectUs Store", description="Here's the ExpectUs **Merchandise Shop** https://shop.spreadshirt.se/expectus/", colour=botColour)
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
        embed.add_field(name="**/info <@User>**", value="Use to find infomation about a specific user.")
        embed.add_field(name="**/report <@User>  <reason>**", value="Use to report someone if they break ExpectUs Rules.")
        embed.add_field(name="**/steam**", value="Use to find the Official ExpectUs Steam group.")
        embed.add_field(name="**/youtube**", value="Use to find the Official ExpectUs Youtube channel.")
        embed.add_field(name="**/twitter**", value="Use to find the Official ExpectUs Twitter.")
        embed.add_field(name="**/suggest <suggestion>**", value="Use this to make suggestions on how we could improve ExpectUs and this discord.")
        embed.add_field(name="**/ingame <game>**", value="Use this to display everyone currently playing a specific game.")
        embed.add_field(name="**/patchnotes**", value="Use to find the latest patch notes for this bot and to check new features.")
        embed.add_field(name="**/store**", value="Use to find the Official ExpectUs shop to support the team.")
        await client.send_message(me, embed=embed)
        await client.delete_message(message)




    if message.content.upper().startswith("/PATCHNOTES") or message.content.upper().startswith("/PN"):
        embed = discord.Embed(title=" ", description=" ", colour=botColour)
        embed.set_author(name="{} Patch Notes".format(version))
        embed.set_thumbnail(url=serverpp)
        embed.set_footer(text="Developer - Cooper#3722")
        embed.add_field(name="- New command: /ingame", value="This is a new functions allowing users to check who is currently playing a specific game. It will display the number of current players aswell as a list of all the players usernames.")
        embed.add_field(name="- Automatic streamer role", value="When ever someone streams on twitch they will be given a 'Streaming' role. This allows streamers within the community to be found more easily. Note, This function will only work if your twitch account has been linked to your discord")
        embed.add_field(name="- New command: /info <@User>", value="This allows users to find out infomation about anyone in the server without having to look yourself.")
        embed.add_field(name="- New command: /store", value="This private messages you a link to the ExpectUs Shop where you can support ExpectUs by purchasing merchandise. '/shop' is an alternative command.")
        


        await client.send_message(me, embed=embed)
        await client.delete_message(message)

##    except:
##        await client.send_message(message.channel, "{} use '/help' to see all valid commands.".format(mention))



    
        
        
        
        
        

client.run("NDU3OTc4Mjk0NTYyNzE3Njk3.DghDhg.mUSLaVRhedFbWSRH0Uh1nrJaYF0")  #starts the bot
