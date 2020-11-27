import time
import os
from subprocess import call
from playsound import playsound

def play_alarm ():
    call(['clear'])
    print ('\n\n        ALARM!')
    playsound('alarms/King_Nothing.MP3')

print ('\n\n        ALARM!')

#playsound('../alarms/King_Nothing.MP3')