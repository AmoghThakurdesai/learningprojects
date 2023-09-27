#! python3
# stopwatch.py - A simple stopwatch program

import time

import pyperclip

# display the programs instructions
log = []
print('Press ENTER to begin.Afterwards, press ENTER to "click" the \
stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()



lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime, 2)
        totalTime = round(time.time()-startTime, 2)
        laprec = f'Lap # {str(lapNum).rjust(3)}:{str(totalTime).rjust(6)}({str(lapTime).rjust(6)})'
        print(laprec, end='')
        log.append(laprec)

        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception and keep its error from displaying
    print('\nDone.')
log = '\n'.join(log)
pyperclip.copy(log)



