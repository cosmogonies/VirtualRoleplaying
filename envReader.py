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



parseEnvFile()