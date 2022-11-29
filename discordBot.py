# bot.py
import os,sys,os.path,pprint
import datetime

print("="*20)
print("discordBot.py START")

import discord
#from dotenv import load_dotenv

import diceManager

import envReader

import re

#load_dotenv()

client = discord.Client()
print('------')

#pprint.pprint(dir(client))

print('------')



@bot.command()
async def janken(ctx):
    





#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return

#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!')

#@client.event
#async def on_message(message):
    # we do not want the bot to reply to itself
#    if message.author == client.user:
#        return

#    if message.content.startswith('!hello'):
#        msg = 'Hello {0.author.mention}'.format(message)
#        await client.send_message(message.channel, msg)


def getNiceName(author):
    if author.nick:
        return str(author.nick)
    else:
        return str(author.name)



def extractMemberIdList(_message):
    import re, pprint

    print("extractMemberIdList(\""+_message+"\");")

    #input_example = "creerChannel <False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=326707820835897354 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>creerChannel <Message id=666 channel=<TextChannel id=860169722556579860 name='capitaine-conteur' position=3 nsfw=False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=666 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>   <Member id=123 n  "
    #pattern = re.compile(r'Member id=([0-9]+)')
    pattern = re.compile(r'@!([0-9]+)')
    resultMatch = pattern.findall(_message)
    print("resultMatch=");
    pprint.pprint(resultMatch)

    memberIdList = []
    for group in resultMatch:
        pprint.pprint(group)
        memberIdList.append(int(group))
    return memberIdList



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    author = message.author

    if message.content.startswith('!janken'):
        print('on_message !janken')
        await doJanken(author, message)

    if message.content.startswith('!test'):
        print('on_message !test')
        await test(author, message)

    if message.content.startswith('!tarot'):
        print('on_message !tarot')
        await doTarot(author, message)

    if message.content.startswith('!challenge simple'):
        await doChallengeSimple(author, message)
    if message.content.startswith('!challenge complexe'):
        await doChallengeComplex(author, message)
    if message.content.startswith('!creerChannel'):
        await doCreateChannel(author, message)


async def test(author, message):
    print('in test function')
    await message.channel.send(F'Hi {getNiceName(author)}, I heard you. Test is success ^^')

#print('in test function')
#username = client.get_user(user_id)

async def doJanken(author, message):
    #Usage: 
    #!janken x666
    #... donnera 666 challenges.

    #Est-ce que le janken est multiples ? (présence de " x" suivi du nombre d'occurence)
    if not " x" in message.content:
        result = diceManager.chooseJanken()
        userNiceName = getNiceName(author) #On veut afficher le pseudo du joueur sur le serveur
        await message.channel.send(userNiceName+' fait '+str(result))

    else:
        occurences = int(message.content.split(' x')[1]) #On transforme la dernière partie de la commance en nombre d'occurences.
        result = []

        # On lance "occurences" fois le dé:
        for i in range(occurences):
            result.append(diceManager.chooseJanken())

        userNiceName = getNiceName(author)
        await message.channel.send(userNiceName+' fait '+str(result))

        #Juste pour vérifier, on affiche les statistiques (éviter les suspicions !)
        await message.channel.send(str(result.count('Pierre'))+"xPierre " + str(result.count('Feuille'))+"xFeuille "+ str(result.count('Ciseau'))+"xCiseau")

        








async def doCreateChannel(author, message):
    print('creerChannel '+str(message))
    print('='*20)
    #channelName= "channelName"

    #userId = "326707820835897354"
    #userId =  326707820835897354
    
    #<Member id=326707820835897354 

    # regexp = "<Message id=([0-9]*) "

    # import re

    # input_example = "creerChannel <Message id=948352591203553290 channel=<TextChannel id=860169722556579860 name='capitaine-conteur' position=3 nsfw=False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=326707820835897354 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>creerChannel <Message id=666 channel=<TextChannel id=860169722556579860 name='capitaine-conteur' position=3 nsfw=False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=326707820835897354 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>"
    # regexp_1 = re.compile(r'<Message id=([0-9]*) ')
    # re_match = regexp_1.match(input_example)
    # for group in re_match.groups():
    #     pprint.pprint(group)

#list(re_match.groups())

    #await message.guild.create_text_channel(channelName)
    #await message.channel.set_permissions(message.author, read_messages=True, send_messages=True)

    #overwritesverwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False),ctx.author: discord.PermissionOverwrite(view_channel=True),your_role: discord.PermissionOverwrite(view_channel=True)}

    # overwrites = {
    #     message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    #     message.guild.me: discord.PermissionOverwrite(read_messages=True)
    # }
    # channel = await message.guild.create_text_channel(channelName, overwrites=overwrites)

    channelName = ""

    prefixDate = datetime.datetime.now().strftime("%b")+(datetime.datetime.now().date().strftime("%Y"))[-2:]
    channelName = prefixDate+"•"

    memberIdList = extractMemberIdList(message.content)
    memberList = []
    for memberId in memberIdList:
        member = await message.guild.fetch_member(memberId) 
        pprint.pprint(member)
        pprint.pprint(member.nick)
        memberList.append(member)

        #channelName += getNiceName(member)[0:3]
        channelName += getNiceName(member).capitalize()[0:3]+"-"

    


    overwrites = {message.guild.default_role: discord.PermissionOverwrite(read_messages=False), message.guild.me: discord.PermissionOverwrite(read_messages=True)}
    newChannel = await message.guild.create_text_channel(channelName, overwrites=overwrites)
    #await newChannel.set_permissions(message.guild.default_role, read_messages=False, send_messages=False)


    for member in memberList:
        await newChannel.set_permissions(member, read_messages=True, send_messages=True)




    await message.channel.send(f"A new channel called '{channelName}' was made")





async def doTarot(author, message):
    result = diceManager.chooseTarotCard()
    await message.channel.send('*'+getNiceName(author)+' tire la carte "'+str(result)+'"*')




async def doChallengeSimple(author, message):
    #result = diceManager.chooseChallengeSimple()
    #await message.channel.send('*'+getNiceName(author)+' obtient "'+str(result)+'"*')
    occurences = 1
    if not " x" in message.content:
        result = diceManager.chooseChallengeSimple()
        await message.channel.send('*'+getNiceName(author)+' obtient "'+str(result)+'"*')
    else:

        occurences = int(message.content.split(' x')[1])
        result = []
        for i in range(occurences):
            result.append(diceManager.chooseChallengeSimple())
        await message.channel.send(getNiceName(author)+' fait '+str(result))

async def doChallengeComplex(author, message):
    #result = diceManager.chooseChallengeComplex()
    #await message.channel.send('*'+getNiceName(author)+' obtient "'+str(result)+'"*')
    occurences = 1
    if not " x" in message.content:
        result = diceManager.chooseChallengeComplex()
        await message.channel.send('*'+getNiceName(author)+' obtient "'+str(result)+'"*')
    else:

        occurences = int(message.content.split(' x')[1])
        result = []
        for i in range(occurences):
            result.append(diceManager.chooseChallengeComplex())
        await message.channel.send(getNiceName(author)+' fait '+str(result))



client.run(envReader.getDiscordToken())
print("discordBot.py END")
