import winreg
import string
import re
openSaveMruPath = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU'



def output_printable(line):
    printable = string.printable
    output = ""
    for letter in line:
        if letter in printable and letter != '\n' and letter != '\t' and letter != '' and letter != '':
            output += letter
    if output == "":
        return ""
    else:
        return output + '\n'


def pull_open_save_mru():
    try:
        # open the registry
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        # open the OpenSavePidlMRU key
        key = winreg.OpenKey(registry, openSaveMruPath)
        returnStr = str()
        # Iterate through all subkeys of OpenSavePidlMRU
        for i in range(0, winreg.QueryInfoKey(key)[0]):
            # Grab Subkey name
            subkeyName = winreg.EnumKey(key, i)
            returnStr += ('Extension: ' + subkeyName + '\n')
            # Grab the subkey with the name
            subkey = winreg.OpenKey(key, subkeyName)
            # Iterate through subkey's subkeys
            for j in range(0, winreg.QueryInfoKey(subkey)[1]):
                value = winreg.EnumValue(subkey,j)[1].decode('utf-16','ignore')
                returnStr += output_printable(value).lstrip(('h1pP.8'))
            # newline for each key entry

        return returnStr
    except Exception as e:
        print(e)

