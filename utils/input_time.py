import time
import os
import datetime


def read_input_time (today):
    try:
        print('please enter time with this format: ' + 'HHMM')
        input_time = datetime.datetime.strptime(input('alarm time: '), '%H%M')
    except:
        print('Please enter the proper format')
    input_time = input_time.replace(year=today.year, month=today.month, day=today.day)
    print (input_time - today)
    if input_time < today:
        new_day_date = today.day + 1
        input_time = input_time.replace(day=new_day_date) #sets the date of alarm for tomorrow, if tthe time is passed today
    else:
        pass
    print ('alarm set to: ', input_time)
    print (input_time)
    target_time = input_time

    return target_time