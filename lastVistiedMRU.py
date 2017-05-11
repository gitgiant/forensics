import winreg
import string

lastVisitedMRUpath = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU'
printable = set(string.ascii_letters)


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


def pull_last_visited_mru():
    try:
        # open the registry
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        # open the OpenSavePidlMRU key
        key = winreg.OpenKey(registry, lastVisitedMRUpath)
        returnStr = ""
        # Iterate through all subkeys of OpenSavePidlMRU
        for i in range(0, winreg.QueryInfoKey(key)[1]):

            value = winreg.EnumValue(key,i)[1].decode("mbcs")

            returnStr += output_printable(value)
        return returnStr
    except Exception as e:
        print(e)
