#! python3
# countdown.py - A simple countdown scripy.

import subprocess
import time

timeLeft=60
while timeLeft>0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
# at the end of countdown play a sound file
subprocess.Popen(['start','alarm.wav'],shell=True)

