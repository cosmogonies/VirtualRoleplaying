import guilded
from guilded.ext import commands
import random

import os, sys
import pprint

import guilded.channel
import guilded.team
import guilded.client

import datetime

import envReader
import diceManager

# The source of this example bot was taken from the examples directory in the
# discord.py repository and modified slightly to demonstrate the similarities
# between the two packages.
# https://github.com/Rapptz/discord.py/blob/master/examples/basic_bot.py

description = '''An example bot to showcase the guilded.ext.commands extension
module, as well as to furthermore demonstrate the similarities between
guilded.py and discord.py.'''

bot = commands.UserbotBot( command_prefix=['?', '||?'], description=description)
#bot = commands.Bot(command_prefix='||?', description=description)

@bot.event
async def on_ready():
    print("="*20)
    print("guilded bot START")
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='Pour vous aider dans vos choix cornéliens')
async def choisir(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(diceManager.chooseBetwween(choices))
    #await ctx.send(random.choice(choices))

@bot.command(description='Tirer une carte de tarot.')
async def tarot(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(diceManager.chooseTarotCard())
    #await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: guilded.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


#======================================================================================
#    pprint.pprint("="*10)
#    pprint.pprint(ctx.author.name)#'Phedre'
#    pprint.pprint(ctx.guild.name)#'altereal'





@bot.command()
async def test(ctx, poolSize: int, difficulty=6):
    """Lancer de dés pour déterminer action à issu incertaine."""

    #Sanity checks:
    if poolSize>10:
        await ctx.send("Votre nombre de dés ne peut pas excéder 10 !")
        return

    success = 0
    detailsFormated = "("
    result = ""

    #print(dir(ctx))
    #print(ctx.prefix)
    isHidden = ctx.prefix.startswith("||")

    pool = []
    for i in range(poolSize):
        pool.append(random.randint(1, 10)) # both included
    pool = sorted(pool)
    for diceRoll in pool:
        if diceRoll == 1:
            success = success - 1
            #detailsFormated +=  " 1 "
            detailsFormated +=  ":1fumble:"
        elif diceRoll >= difficulty:
            success = success + 1
            detailsFormated +=  " **"+str(diceRoll)+"** "
        else:
            detailsFormated+= str(diceRoll)
        detailsFormated+=","
    detailsFormated =detailsFormated[:-1] #removing last ","
    detailsFormated+=")"

    if(isHidden):
        detailsFormated=""

    if(success==0):
        result = "Résultat: échec... "+detailsFormated
    elif(success<0):
        result = "Résultat: **ECHEC CRITIQUE** !!! "+detailsFormated
    else:
        result = "Résultat: *"+str(success)+ "* succès ! "+detailsFormated

    await ctx.send(result)








#gon's own command
@bot.command()
async def backupChannels(ctx, channelName='Charte'):
    """Backup a channel."""

    print("server has "+str(len(ctx.guild.channels))+" channels.")

    backupedDict = {}

    #f = open("testFile.txt", "w")
    #f.write("Now the file has more content!")
    #f.close()

    #member = await message.guild.fetch_member(memberId) 
    #pprint.pprint(member)

    timeStampSuffix = datetime.datetime.now().strftime("%y-%m-%d_%Hh-%Mm-%Ss")

    backupDirPath = "backups/"+timeStampSuffix
    os.mkdir(backupDirPath)

    #dBW3YqPm
    #41WeQkMm
    # member = await ctx.guild.fetch_member("dBW3YqPm")
    # print("member="+str(member))
    # print("member.name="+str(member.name))
    # print("member.nick="+str(member.nick))
    # pprint.pprint(dir(member.nick))
    #print("member.display_name="+str(member.display_name))
    
    #pprint.pprint(dir(member))

    #print("member.stop="+str(member.stop))

    knownUsers = {}


    for channel in ctx.guild.channels:

        pprint.pprint("<"+str(channel.type)+"> "+str(channel.name))

        #if str(channel.type) == 'ChannelType.chat':
        if str(channel.type) == 'chat':




            historyBuffer = await channel.history()
            pprint.pprint("<"+str(channel.type)+"> "+str(channel.name)+" with "+str(len(historyBuffer))+" messages.")
            backupedDict[str(channel.name)] = []


            #fileDesc = open(backupDirPath+"/"+str(channel.name)+" ("+timeStampSuffix+").csv", "w")
            fileDesc = open(backupDirPath+"/"+str(channel.name)+" ("+timeStampSuffix+").xml", "w")
            fileDesc.write("<root>")

            for message in historyBuffer:
                #pprint.pprint(dir(message)) 
                #messageContent = str(message)
                #print(messageContent)
                #backupedDict[str(channel.name)].append(messageContent)

                #pprint.pprint(dir(message.author))

                messageTime = str(message.created_at.strftime("%y-%m-%d_%Hh-%Mm-%Ss"))

                authorId = message.author_id
                authorName = "No0ne"
                if(authorId in knownUsers):
                    authorName = knownUsers[authorId]
                else:
                    member = await ctx.guild.fetch_member(authorId)
                    #authorName = member.name
                    authorName = getMemberNiceName(member)
                    knownUsers[authorId] = authorName

                
                #fileDesc.write(str(message.created_at.strftime("%y-%m-%d_%Hh-%Mm-%Ss"))+"|"+str(message.author)+"|"+str(message.author_id) +"|<<"+str(message.content)+">>")
                #fileDesc.write(messageTime + "|" + authorName +"|<<"+str(message.content)+">>")
                #fileDesc.write(messageTime + "|" + authorName +"|<<"+str(message.content)+">>")
                fileDesc.write("    <Message date=\""+messageTime + "\" author=\"" + authorName +"\">"+str(message.content)+"</Message>")
            
            fileDesc.write("</root>")
            fileDesc.close()
            #await ctx.send("<"+str(channel.type)+"> "+str(channel.name)+" backuped with "+str(len(historyBuffer))+" messages.")


        if str(channel.type) == 'ChannelType.announcement': #<ChannelType.announcement> 
            #pprint.pprint(dir(channel)) 
            #pprint.pprint(help(channel.announcements))
            historyBuffer = await channel.fetch_announcements()
            #historyBuffer = channel.announcements
            pprint.pprint("<"+str(channel.type)+"> "+str(channel.name)+" with "+str(len(historyBuffer))+" announcements.")


            backupedDict[str(channel.name)] = []
            for message in historyBuffer:
                #pprint.pprint(dir(message)) 
                pprint.pprint(message.title) 
                messageContent = str(message.content)
                #print(messageContent)

                #key = str(channel.name.replace('@','at').encode('ascii', 'ignore'))
                #key = str(channel.name.replace('@','at').replace(' ','_'))
                #key = key.encode('ascii', 'ignore').decode('ascii') #removing unicode
                backupedDict[str(channel.name)].append(messageContent)


    #timeStampSuffix = datetime.datetime.now().strftime("%y-%m-%d_%Hh-%Mm-%Ss")

    #backupDirPath = "backups/"+timeStampSuffix
    #os.mkdir(backupDirPath)

    # for key, value in backupedDict.items():
    #     f = open(key+" _"+timeStampSuffix+".txt", "w")

    #     f.write(str(key))
    #     for message in value:
    #         f.write("\t"+str(message))
    #     #f.write("Now the file has more content!")
    #     f.close()


    await ctx.send(str(len(backupedDict))+" channels backuped")
            

@bot.command()
async def GetUserRankByPost(ctx):
    """  """
    print("GetUserRankByPost")
    knownUsers = {}
    authorDict = {}

    currentMonth = datetime.datetime.now().month
    currentYear = datetime.datetime.now().year
    print("currentMonth ="+str(currentMonth))
    print("currentYear ="+str(currentYear))

    #pprint.pprint(dir(ctx.guild))
    #return

    #for test in ctx.guild._threads:
    #    print("toto")
    #return

    for channel in ctx.guild.channels:
        pprint.pprint("<"+str(channel.type)+"> "+str(channel.name))
    return

    for channel in ctx.guild.channels:
        #print(channel.name)
        #pprint.pprint("<"+str(channel.type)+"> "+str(channel.name))

        if str(channel.type) == 'chat':

            #historyBuffer = await channel.history(None,None,50,False)
            #historyBuffer = await channel.history(include_private=False)

            print("dir(channel)")
            pprint.pprint(dir(channel))
            return
             

            try:
                historyBuffer = await channel.history()
                pprint.pprint("<"+str(channel.type)+"> "+str(channel.name)+" with "+str(len(historyBuffer))+" messages.")

                for message in historyBuffer:

                    #pprint.pprint(str(message.content))

                    messageTime = message.created_at

                    print("MessageMonth ="+str(messageTime.month))

                    if messageTime.year == currentYear:
                        if messageTime.month == currentMonth:

                            

                            authorId = message.author_id
                            authorName = "No0ne"
                            if(authorId in knownUsers):
                                authorName = knownUsers[authorId]
                            else:
                                member = await ctx.guild.fetch_member(authorId)
                                authorName = getMemberNiceName(member)
                                knownUsers[authorId] = authorName

            except: 
                continue





    


@bot.command()
async def GetChannel(ctx, channelName):
    """  """
    #pprint.pprint(dir(ctx))
    pprint.pprint(dir(ctx.guild))

    print("groups:")
    for currentGroup in ctx.guild.groups:
        print("\t"+currentGroup.name)

    print("channels:")
    for currentChannel in ctx.guild.channels:
        print("\t"+currentChannel.name+" <"+str(currentChannel.type)+">")

 #   print("fetch channels:")
 #   channelBuffer = await ctx.guild.fetch_channels()
 #   for currentChannel in channelBuffer:
 #       print("\t"+currentChannel.name+" <"+str(currentChannel.type)+">")
    #print("fetching one:")
    #https://www.guilded.gg/altereal/groups/53NlV0bd/channels/d446c4bc-1f3a-4e36-89b4-f908abda859f/chat
    #channelTest = await ctx.guild.fetch_channel("Pr.Exemple")
    #channelTest = await ctx.guild.fetch_channel("d446c4bc-1f3a-4e36-89b4-f908abda859f")
    #pprint.pprint(channelTest.name)


    print("server has "+str(len(ctx.guild.channels))+" channels.")

    for channel in ctx.guild.channels:
        #pprint.pprint("<"+str(channel.type)+"> "+str(channel.name))

        #pprint.pprint(type(channel.group))
        
        #pprint.pprint(dir(channel.group))
        #pprint.pprint("<"+str(channel.type)+"> ["+str(channel.group.name)+"] "+str(channel.name)+" FOUND")

#        #if str(channel.type) == 'ChannelType.ChannelType.forum':
#        if (channel.name== "Feuille de personnage"): #AnnouncementChannel
#            print(channelName+" is found.")
#            pprint.pprint(dir(channel))
#            print("="*20)
#            print("it has "+str(len(channel.announcements))+ "annoncements") #it has 0annoncements
#            #historyBuffer = await channel.announcements
#            for message in channel.announcements:
#                #pprint.pprint(dir(message)) 
#                messageContent = str(message)
#                print(messageContent)      


        if(channel.name == channelName):          
            return channel
  
            

        
#        if (channel.name== "Feuille de perso"):
#            print("Feuille de perso is found.")

            #for topic in channel.topics:
#            historyBuffer = await channel.history()
            #pprint.pprint(dir(historyBuffer))
#            pprint.pprint("Feuille de perso.history.count="+ str(len(historyBuffer)))

#            for message in historyBuffer:
                #pprint.pprint(dir(message)) 
#                messageContent = str(message)
#                print(messageContent)

    print("Channel (named:"+channelName+") not found, please check if the bot has correct rights !")
    await ctx.send("Channel (named:"+channelName+") not found, please check if the bot has correct rights !")
              




@bot.command()
async def createCharacter(ctx, characterName='nobody'):
    """Create all forum/topics required for a newly character."""

    #Find the characters category:
    #pprint.pprint(dir(ctx.guild))
    #for channel in ctx.guild.channels:
    #for test in ctx.guild.subdomain:
    #    print(test)

    #charChannel = await createChannel(ctx, channelName=characterName, categoryName='Seul avec le conte')    
    charChannel = await createChannel(ctx, channelName=characterName)

    tutorialMessageText = "\n\
    Dans ce channel, vous pouvez discuter librement en toute aparté avec le conte,\n\
    pour toutes questions secrètes vis à vis de votre histoire, votre jeu/interprétation mais aussi des questions (secrètes) de règles."
    tutorialMessage = await charChannel.send(tutorialMessageText)
    await tutorialMessage.pin()


    topicDict={}
    topicDict["Feuille de personnage"]="Une fois votre feuille de personnage validée, elle sera affichée ici, en thread locké.\n\
    https://www.guilded.gg/altereal/groups/PdY5YKKd/channels/cf05635c-84cd-41b5-8e35-090e802404dd/announcements\n\
    https://www.guilded.gg/altereal/groups/PdY5YKKd/channels/e83d76ba-0c69-4c36-b610-69f98e970979/docs/281472"

    topicDict["Progression (leveling)"]="Ici se tiendra l'historique complet de l'évolution de votre fiche.\n\
    A la fois vos gains d'experiences, mais aussi leurs dépenses, mois par mois."

    topicDict["Journal"]="\n\
    Journal de bord de votre personnage.\n\
    Insérer ici d'abord l'histoire de votre personnage (background).\n\
    Puis cet espace vous servira de memo pour les périgrinations vécues !"
    topicDict["Relations"]="\n\
    Inscrivez ici vos descriptions fluff de vos historiques, et des personnages que vous croisez.\n\
    Ce forum peut aussi servir de memo pour indiquer ce que votre personnage pense des autres des personnages que vous croisez, que ce soit par amour, amitié, indifférence ou haine farouche."
    topicDict["Possessions"]="\n\
    Indiquez ici vos acquisitions matérielles notables, avec description fluff si possible ^^.\n\
    C'est ici que sera indiqué vos possessions matérielles exceptionnelles, des lieux en votre contrôle via les historiques aux objets inhabituels acquis au cours de l'histoire.\n\
    En particulier pour les lieux publics possédés (bar, club, assos, etc.) via l'historique Ressources."
    topicDict["Actions mensuelles"]="\n\
Entrez ici, chaque mois, vos actions étendues de votre personnage.\n\
Rappel: date limite de rendu: le dernier jour du mois, à minuit! (Heure de Paris GMT+1)\n\
https://www.guilded.gg/altereal/groups/PdY5YKKd/channels/e83d76ba-0c69-4c36-b610-69f98e970979/docs/276806\n\
\n\
Activités pour le Mois: MM - YYYY *(ex: mars - 2022)*\n\
Activité 1 : ...............\n\
Activité 2 : ...............\n\
Activité 3 : ...............\n\
Activité 4 : ...............\n\
Activité 5 : ..............."


    baseForum = await createForum(ctx, characterName+" - Suivi", topicDict)

    await ctx.send("Character (named:"+characterName+") created !")



#async def createForum(ctx, forumName='forumName', firstTopic='firstTopicName', secondTopic='secondTopicName', content ='test content'):
async def createForum(ctx, forumName='forumName', topicDict={}):
    """Create all forum/topics required for a newly character."""
    
    newForumChannel = await ctx.guild.create_forum_channel(name=forumName)

    for topicTitle in topicDict:
        topicContent = topicDict[topicTitle]
        await newForumChannel.create_topic(topicContent, title=topicTitle)
    #await newForumChannel.create_topic('placeHolder', title='firstTopic')
    #await newForumChannel.create_topic(title = 'secondTopic', content = 'placeHolder')


#gon's own command


@bot.command()
async def createChannel(ctx, channelName='defaultChannelName', groupName = 'CONTE'):
    """Create a simpleChannel."""
    """Usage:  ?createChannel channelName"""

    #return await ctx.guild.create_chat_channel(name=channelName)


    #print("dir(ctx.guild)")
    #pprint.pprint(dir(ctx.guild))
    group = None

    for currentGroup in ctx.guild.groups:
        print(currentGroup.name+","+str(currentGroup.id))

        if(currentGroup.name.lower() == groupName.lower()):
            group = currentGroup



    return await ctx.guild.create_chat_channel(name=channelName, category=None, public=False, group=group)
    #return await ctx.send("Cette fonction ne marche pas (encore)")



@bot.command()
async def debugMe(ctx):#, channelName='channelName'):
    """Usage:  ?debugMe Pr.Exemple"""
    #testChannel = await GetChannel(ctx, "Pr.Exemple")
    #pprint.pprint(dir(testChannel))
    #testMessage = await testChannel.send("test")
    #await testMessage.pin()

    #print("dir(ctx.guild)")
    #pprint.pprint(dir(ctx.guild))


    pprint.pprint(sys.modules)

    print("chat")

    #testMessage = await testChannel.send( MessageForm("test") )


@bot.command()
async def listUsers(ctx):
    #print("dir(ctx.guild)")
    #pprint.pprint(dir(ctx.guild))

    for currentMember in ctx.guild.members:

        #pprint(help(currentMember))

        #pprint(dir(currentMember))
        print("_"*20)

        print(currentMember.nick)
        print(currentMember.display_name)
        print(currentMember.id)
        print(currentMember.name)

def getMemberNiceName(_member):
    # print("_"*20)

    # print(currentMember.nick)
    # print(currentMember.display_name)
    # print(currentMember.id)
    # print(currentMember.name)
    if currentMember.nick == None:
        return currentMember.display_name


@bot.command()
async def doStuff(ctx, _context):

    print(str(_context))

    # for currentGroup in ctx.guild.groups:
    #     print(currentGroup.name)


    # print("channels:")
    # for currentChannel in ctx.guild.channels:
    #     print("\t"+currentChannel.name+" <"+str(currentChannel.type)+">")

    #     if currentChannel.name == "Prime":
    #         await ctx.send("Channel hyperlink: #"+currentChannel.name+")")

    await ctx.send("Channel hyperlink: <#088a916a-4174-4f6d-af60-4354934e2cea>)")
    #import characters
    #print(dir(characters))




# @bot.command()
# async def createFormAM(ctx):

#     #print(dir(ctx))
#     #newForumChannel = await ctx.guild.create_forum_channel(name=forumName)

#     currentChannel = ctx.channel

#     print(dir(currentChannel))

#     currentChannel.send("test")

#     myForm = MessageForm("toto")
#     currentChannel.send(myForm)




@bot.command()
async def reload(ctx):
    """Reload python commands."""
    import importlib
    import sys
    #pprint.pprint(sys.modules)
    #reload(sys.modules['__main__'])

    #import imp
    #imp.load_module('__main__',*imp.find_module('__main__'))

    #import importlib
    #importlib.reload(sys.modules['__main__'])

    #reload(altereal)
    #reload(sys.modules['altereal'])

    #print("Python modules reloaded !!")
    #await ctx.send("Python modules reloaded !!")
    await ctx.send("Cette fonction ne marche pas (encore)")


#bot.run(envReader.getGuildedLogin(), envReader.getGuildedToken())

