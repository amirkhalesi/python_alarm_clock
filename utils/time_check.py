import datetime
import time
import sys
import os
from subprocess import call
from utils.play_alarm import play_alarm

def time_check (target_time):
    while True:
        call(['clear'])
        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime('%H:%M:%S')
        time_remaining = target_time - current_time
        print ('time remaining to alarm: ', time_remaining)
        print ('\ncurrent time is: ', current_time_string)
        time.sleep(1)
        if target_time >= current_time:
            pass
        else:
            break
