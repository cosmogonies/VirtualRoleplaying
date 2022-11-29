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


getDiscordToken():
    credentialDict = parseEnvFile()

    if 'DISCORD_TOKEN_ALTEREAL' in credentialDict:
        return credentialDict['DISCORD_TOKEN_ALTEREAL']
    else:
        print("ERROR: Cannot find key 'DISCORD_TOKEN_ALTEREAL' in creadentials in .env file !")
        return ''

getGuildedLogin():
    credentialDict = parseEnvFile()

    if 'GUILDED_LOGIN' in credentialDict:
        return credentialDict['GUILDED_LOGIN']
    else:
        print("ERROR: Cannot find key 'GUILDED_LOGIN' in creadentials in .env file !")
        return ''


getGuildedToken():
    credentialDict = parseEnvFile()

    if 'GUILDED_TOKEN' in credentialDict:
        return credentialDict['GUILDED_TOKEN']
    else:
        print("ERROR: Cannot find key 'GUILDED_TOKEN' in creadentials in .env file !")
        return ''


#parseEnvFile()