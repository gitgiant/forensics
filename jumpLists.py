import os
path = os.environ['USERPROFILE'] + '\AppData\Roaming\Microsoft\Windows\Recent\\'


def pull_jump_lists():
    returnStr = "***Jump Lists***\n"
    for i in os.listdir(path):
        returnStr += i + '\n'
    return returnStr