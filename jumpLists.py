import os
path = os.environ['USERPROFILE'] + '\AppData\Roaming\Microsoft\Windows\Recent\\'
def pull_jump_lists():
    for i in os.listdir(path):
        print(i)
