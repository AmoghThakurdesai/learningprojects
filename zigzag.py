# Write your code here :-)
import time,sys
indent=0#spaces to indent
indentIncreasing=True

try:
    while True:
        print(' '*indent,end='')
        print('********')
        time.sleep(0.1)#pause for 0.1sec
        if indentIncreasing:
        #increase no of spaces
            indent=indent+1
            if indent==20:
                indentIncreasing=False#change direction
        else :
            indent=indent-1
            if indent==0:
                indentIncreasing=True#change direction
except KeyboardInterrupt:
    sys.exit()
