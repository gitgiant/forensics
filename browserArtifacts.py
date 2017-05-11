# TODO implement for other browsers
import os
path = os.environ['USERPROFILE'] + '\AppData\Local\Google\Chrome\\User Data\Default\History'

def pull_chrome_artifacts():
     f = open(path, 'r', encoding="mbcs")
     for line in f:
          print(line)