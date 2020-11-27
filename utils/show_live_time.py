import time
import datetime
import os
import sys

def show_live_time():
    print ('current time')
    print (time.strftime('%H:%M:%S'))
    today = datetime.datetime.now()
    print (today.date())

    return today
    #ctime shows the current time