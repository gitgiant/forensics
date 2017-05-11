import winreg
import string

lastVisitedMRUpath = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU'
printable = set(string.ascii_letters)

# TODO only output legit characters
def pull_run_mru():
    try:
        # open the registry
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        # open the OpenSavePidlMRU key
        key = winreg.OpenKey(registry, lastVisitedMRUpath)
        returnStr = "***Run Command History***\n"

        # Iterate through all subkeys of OpenSavePidlMRU
        for i in range(0, winreg.QueryInfoKey(key)[1]):
            returnStr += (winreg.EnumValue(key,i)[1] + '\n')
        return returnStr
    except Exception as e:
        print(e)