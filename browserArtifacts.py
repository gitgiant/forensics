# TODO implement for other browsers
import os
import string
path = os.environ['USERPROFILE'] + '\AppData\Local\Google\Chrome\\User Data\Default\History'

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

def pull_chrome_artifacts():
    f = open(path, 'r', encoding="mbcs")
    returnStr = "***Browser Artifacts***\n"
    for line in f:
        returnStr += output_printable(line)
    return returnStr