# bot.py
import os, sys, os.path, pprint
import datetime
import re

# Flusing the log of server console:
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("\n\r");
print("_" * 50)
print("discordBot.py START")
print("_" * 50)

import discord
import discord.ui
import discord.ext
import discord.ext.commands
import discord.app_commands

import envReader

import userManager
import diceManager

intents = discord.Intents.default()  # intents = discord.Intents.all()
intents.message_content = True

MY_GUILD_ID = 925077075356950589

# adminBot = discord.ext.commands.Bot(command_prefix='!', intents=intents)

# client = discord.Client(intents=intents)
# tree = discord.app_commands.CommandTree(client)


client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


# ______________________________
# APP slash category

# @tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=MY_GUILD_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
# async def first_command(interaction):
#     await interaction.response.send_message("Hello!")

# @tree.command(name = "ping", description = "sent PING ? receive PONG !", guild=discord.Object(id=MY_GUILD_ID))
# async def doPing(interaction):
#     await interaction.response.send_message("PONG!")

# ______________________________


@tree.command(name="choisir", description="Permet de choisir entre plusieurs choix !",
              guild=discord.Object(id=MY_GUILD_ID))
async def doChoose(interaction, arg1: str, arg2: str):
    """Chooses between multiple choices."""
    # print("arg1="+str(arg1))
    # choices = ctx. .message.content.split(' ')
    # choices.pop(0)
    await interaction.response.send_message(diceManager.chooseBetwween([arg1, arg2])[0])
    # await interaction.response.send_message("chosen")


# JANKEN_LIST = ["Pierre","Feuille","Ciseau"]
@tree.command(name="challenge", description="MET: tire un pierre/feuille/ciseau", guild=discord.Object(id=MY_GUILD_ID))
async def doJanken(interaction):
    await interaction.response.send_message(diceManager.chooseJanken())


@tree.command(name="challenges", description="MET: tire plusieurs pierre/feuille/ciseau",
              guild=discord.Object(id=MY_GUILD_ID))
async def doJanken(interaction, occurences: int):
    result = []
    # On lance "occurences" fois le dé:
    for i in range(occurences):
        result.append(diceManager.chooseJanken())
    # userNiceName = getNiceName(interaction.response.)
    userNiceName = "YOU"
    await interaction.response.send_message(userNiceName + ' fait ' + str(result))

    # Juste pour vérifier, on affiche les statistiques (éviter les suspicions !)
    # await message.channel.send(
    #     str(result.count('Pierre')) + "xPierre " + str(result.count('Feuille')) + "xFeuille " + str(
    #         result.count('Ciseau')) + "xCiseau")


@tree.command(name="tarot", description="Tire une lame de tarot au hasard🃏", guild=discord.Object(id=MY_GUILD_ID))
async def doTarot(interaction):
    result = diceManager.chooseTarotCard()
    who = userManager.getNiceName(interaction.user)
    message = '*' + str(who) + ' tire la carte "' + str(result) + '"*'
    await interaction.response.send_message(message)


@tree.command(name="test", description="Test un score face à une difficulté. ", guild=discord.Object(id=MY_GUILD_ID))
async def doTest(interaction, score: int, difficulté: int):
    import random

    result = ""

    # Sanity checks:
    if score > 10:
        result = "Votre nombre de dés ne peut pas excéder 10 !"
    else:

        success = 0
        detailsFormated = "("

        # isHidden = message.content.startswith("/test ||")

        pool = []
        for i in range(score):
            pool.append(random.randint(1, 10))  # both included
        pool = sorted(pool)
        for diceRoll in pool:
            if diceRoll == 1:
                success = success - 1
                detailsFormated += " 1 "
                # detailsFormated +=  ":1fumble:"
            elif diceRoll >= difficulté:
                success = success + 1
                detailsFormated += " **" + str(diceRoll) + "** "
            else:
                detailsFormated += str(diceRoll)
            detailsFormated += ","
        detailsFormated = detailsFormated[:-1]  # removing last ","
        detailsFormated += ")"

        # if (isHidden):
        #    detailsFormated = "||" + detailsFormated + "||"

        if (success == 0):
            result = "Résultat: échec... " + detailsFormated
        elif success < 0:
            result = "Résultat: **ECHEC CRITIQUE** !!! " + detailsFormated
        else:
            result = "Résultat: *" + str(success) + "* succès ! " + detailsFormated

    await interaction.response.send_message(result)


@tree.command(name="roll", description="Lance des 🎲dés à x faces . ", guild=discord.Object(id=MY_GUILD_ID))
async def doRoll(interaction, nombre_de_dés: int, nombre_de_faces: int):
    import random

    result = ', '.join(str(random.randint(1, nombre_de_faces)) for r in range(nombre_de_dés))
    await interaction.response.send_message(result)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=MY_GUILD_ID))
    print("on_ready Callback: tree synced")





# ADMIN
# @adminBot.command()
# async def reloadPython(ctx):
#     """Reload python commands."""
#     import sys, importlib
#
#     import pprint
#     # pprint.pprint(sys.modules)
#     # reload(sys.modules['__main__'])
#
#     # import imp
#     # imp.load_module('__main__',*imp.find_module('__main__'))
#
#     # importlib.reload(sys.modules['__main__'])
#     # importlib.reload(sys.modules['discordBot'])
#
#     print("CACA")
#     await ctx.send("Cette fonction ne marche pas (encore)")
#
# @adminBot.command()
# async def getId(ctx):
#     """Chooses between multiple choices."""
#
#     await ctx.send("Guild ID = " + str(ctx.message.guild.id))


async def doCreateChannel(author, message):
    print('creerChannel ' + str(message))
    print('=' * 20)
    # channelName= "channelName"

    # userId = "326707820835897354"
    # userId =  326707820835897354

    # <Member id=326707820835897354

    # regexp = "<Message id=([0-9]*) "

    # import re

    # input_example = "creerChannel <Message id=948352591203553290 channel=<TextChannel id=860169722556579860 name='capitaine-conteur' position=3 nsfw=False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=326707820835897354 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>creerChannel <Message id=666 channel=<TextChannel id=860169722556579860 name='capitaine-conteur' position=3 nsfw=False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=326707820835897354 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>"
    # regexp_1 = re.compile(r'<Message id=([0-9]*) ')
    # re_match = regexp_1.match(input_example)
    # for group in re_match.groups():
    #     pprint.pprint(group)

    # list(re_match.groups())

    # await message.guild.create_text_channel(channelName)
    # await message.channel.set_permissions(message.author, read_messages=True, send_messages=True)

    # overwritesverwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False),ctx.author: discord.PermissionOverwrite(view_channel=True),your_role: discord.PermissionOverwrite(view_channel=True)}

    # overwrites = {
    #     message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    #     message.guild.me: discord.PermissionOverwrite(read_messages=True)
    # }
    # channel = await message.guild.create_text_channel(channelName, overwrites=overwrites)

    channelName = ""

    prefixDate = datetime.datetime.now().strftime("%b") + (datetime.datetime.now().date().strftime("%Y"))[-2:]
    channelName = prefixDate + "•"

    memberIdList = userManager.extractMemberIdList(message.content)
    memberList = []
    for memberId in memberIdList:
        member = await message.guild.fetch_member(memberId)
        pprint.pprint(member)
        pprint.pprint(member.nick)
        memberList.append(member)

        # channelName += getNiceName(member)[0:3]
        channelName += userManager.getNiceName(member).capitalize()[0:3] + "-"

    overwrites = {message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                  message.guild.me: discord.PermissionOverwrite(read_messages=True)}
    newChannel = await message.guild.create_text_channel(channelName, overwrites=overwrites)
    # await newChannel.set_permissions(message.guild.default_role, read_messages=False, send_messages=False)

    for member in memberList:
        await newChannel.set_permissions(member, read_messages=True, send_messages=True)

    await message.channel.send(f"A new channel called '{channelName}' was made")


async def doChallengeSimple(author, message):
    # result = diceManager.chooseChallengeSimple()
    # await message.channel.send('*'+getNiceName(author)+' obtient "'+str(result)+'"*')
    occurences = 1
    if not " x" in message.content:
        result = diceManager.chooseChallengeSimple()
        await message.channel.send('*' + userManager.getNiceName(author) + ' obtient "' + str(result) + '"*')
    else:

        occurences = int(message.content.split(' x')[1])
        result = []
        for i in range(occurences):
            result.append(diceManager.chooseChallengeSimple())
        await message.channel.send(userManager.getNiceName(author) + ' fait ' + str(result))


async def doChallengeComplex(author, message):
    # result = diceManager.chooseChallengeComplex()
    # await message.channel.send('*'+getNiceName(author)+' obtient "'+str(result)+'"*')
    occurences = 1
    if not " x" in message.content:
        result = diceManager.chooseChallengeComplex()
        await message.channel.send('*' + userManager.getNiceName(author) + ' obtient "' + str(result) + '"*')
    else:

        occurences = int(message.content.split(' x')[1])
        result = []
        for i in range(occurences):
            result.append(diceManager.chooseChallengeComplex())
        await message.channel.send(userManager.getNiceName(author) + ' fait ' + str(result))





#ADMIN COMMAND
@client.event
async def on_message(message):
    print("on_message callback")
    if message.content.startswith('/backup'):
    #if message.content.contains('backup'):
        print("on_message callback, calling doBackupFull")
        await doBackupFull(message.author, message)

    if message.content.startswith('/chartify'):
        await doChartifyUsers(message.author, message)


async def doBackupFull(author, message):
    # Source = https://github.com/HTSTEM/DiscordBackup/blob/master/backup.py

    fd = open("./backups/backup"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".csv",'w')

    fd.write("ChannelID|ChannelName|MessageAuthorID|MessageAuthorNick|MessageID|MessageCreationDate|MessageContent")

    guild = message.guild
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):

            #print("\nchannel.id=" + str(channel.id))
            #print("\nchannel.position=" + str(channel.position))
            #print("\nchannel.name=" + str(channel.name))
            #print("\nchannel.topic=" + str(channel.topic))
            #print("\nchannel.type=" + str(channel.type))

            fd.write('\n'+str(channel.id)+'|'+str(channel.name))

            if channel.permissions_for(guild.get_member(client.user.id)).read_message_history:

                after = datetime.datetime(2015, 3, 1)
                async for message in channel.history(limit=None, after=after):
                    #print("\n\tmessage.author.id=" + str(message.author.id))
                    #print("\n\tmessage.id=" + str(message.id))
                    #print("\n\tmessage.content=" + str(message.content))
                    #print("\n\tmessage.created_at=" + str(message.created_at))

                    fd.write('\n||'+str(message.author.id) + '|' +str(message.author.name) +'|'+ str(message.id) + '|'+str(message.created_at)+'|'+"\""+str(message.content).replace('"','\'')+"\"")

                # print("\rLogging {0}: [DONE]            ".format(channel.name))
    fd.close()
    print("backup FULL created")


async def doChartifyUsers(author, message):

    UserMessageCountDict = {}

    guild = message.guild
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            if channel.permissions_for(guild.get_member(client.user.id)).read_message_history:
                after = datetime.datetime(2015, 3, 1)
                async for message in channel.history(limit=None, after=after):

                    if message.author in UserMessageCountDict.keys():
                        UserMessageCountDict[message.author] = UserMessageCountDict[message.author] + 1
                    else:
                        UserMessageCountDict[message.author] = 1

    for key in UserMessageCountDict.keys():
        print("\t"+str(key.name)+'='+str(UserMessageCountDict[key]))






                # BUTTONS TESTS


class DeleteEmbedView(discord.ui.View):
    @discord.ui.button(label='I joined', style=discord.ButtonStyle.green)
    async def delete(self, button: discord.ui.Button, interaction: discord.Interaction):
        # This is called once the button is clicked
        await interaction.message.delete()  # delete the message with the embed
        # delete it from the JSON file here
        # and then whenever you want to send the button with the message do:


#
# @client.event
# async def on_message(message):
#
#     if message.content.startswith('/carte'):
#         #await message.channel.send("test")
#
#         embed=discord.Embed(title="Carte", url="https://www.google.com/maps/d/edit?mid=1hYa4MAOTJ17j_9q4Vf9yVXF7Tr3RS3jn&ll=37.751537613728445%2C-122.45122604998403&z=13", description="Voici le lien (externe) vers la carte interactive de San-Francisco EN-JEU.", color=0xFF5733)
#         await message.channel.send(embed=embed)
#
#     if message.content.startswith('/embed_demo'):
#         #### Create the initial embed object ####
#         embed = discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/",
#                               description="This is an embed that will show how to build an embed and the different components",
#                               color=0x109319)
#
#         # Add author, thumbnail, fields, and footer to the embed
#         embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData",
#                          icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")
#
#         embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
#
#         embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.",inline=False)
#         embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
#         embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
#
#         embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
#
#         #### Useful ctx variables ####
#         ## User's display name in the server
#         #message.channel.author.display_name
#
#         ## User's avatar URL
#         #message.channel.author.avatar_url
#
#         await message.channel.send(embed=embed)
#
#     if message.content.startswith('/button'):
#
#         embed = discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/",
#                               description="This is an embed that will show how to build an embed and the different components",
#                               color=0x109319)
#         #await message.channel.send(embed=embed)
#         await message.channel.send(embed=embed, view=DeleteEmbedView())
#
#         # BUTTONS TESTS
#
#         # formatedMessage = '{\
#         #             "content": "This is a message with components",\
#         #             "components": [\
#         #                 {\
#         #                     "type": 1,\
#         #                     "components": [\
#         #                         {\
#         #                             "type": 2,\
#         #                             "label": "Click me!",\
#         #                             "style": 1,\
#         #                             "custom_id": "click_one"\
#         #                         }\
#         #                     ]\
#         #                 }\
#         #             ]\
#         #         }'
#         #
#
#


# print(envReader.getDiscordToken())
# client.run(envReader.getDiscordToken())

# slashClient.run(envReader.getDiscordToken())

# client.run(envReader.getDiscordToken())

# bot.run(envReader.getDiscordToken())


client.run(envReader.getDiscordToken())

print("_" * 50)
print("discordBot.py END")
print("_" * 50)
