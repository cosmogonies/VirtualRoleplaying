import os, os.path


ENV_FILE_PATH = '.env'

def checkIfEnvExists():
    return os.path.exists()



def parseEnvFile():

    resultAsDict = {}

    if(checkIfEnvExists):
        f = open(ENV_FILE_PATH, "r")
        lines = f.readlines()
        #print(lines)
        for line in lines:
            print(line)

            if '=' in line:
                key = line.split('=')[0]

                value = line.split('=')[1]

                lastIndex = value.index("'",1)

                value = value[1:lastIndex]

                print((key, value))
                resultAsDict[key] = value

    return resultAsDict


def getDiscordToken():
    credentialDict = parseEnvFile()

    if 'DISCORD_TOKEN_ALTEREAL' in credentialDict:
        print("Discord tokens found ^^")
        return credentialDict['DISCORD_TOKEN_ALTEREAL']
    else:
        print("ERROR: Cannot find key 'DISCORD_TOKEN_ALTEREAL' in credentials in .env file !")
        return ''

def getGuildedLogin():
    credentialDict = parseEnvFile()

    if 'GUILDED_LOGIN' in credentialDict:
        return credentialDict['GUILDED_LOGIN']
    else:
        print("ERROR: Cannot find key 'GUILDED_LOGIN' in credentials in .env file !")
        return ''



def getGuildedToken():
    credentialDict = parseEnvFile()

    if 'GUILDED_TOKEN' in credentialDict:
        return credentialDict['GUILDED_TOKEN']
    else:
        print("ERROR: Cannot find key 'GUILDED_TOKEN' in credentials in .env file !")
        return ''


parseEnvFile()
print(getDiscordToken())