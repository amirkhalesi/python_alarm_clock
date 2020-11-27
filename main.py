import time
import datetime
from subprocess import call
from utils.input_time import read_input_time
from utils.play_alarm import play_alarm
from utils.time_check import time_check
from utils.show_live_time import show_live_time



def main():
    target_time = 1
    call(['clear'])  # uses a subprocess to show you the time
    print('welcome to chomagh!')

    today = show_live_time()
    time.sleep(1)

    target_time = read_input_time(today)

    time_check(target_time)

    play_alarm()

if __name__ == '__main__':
    main()