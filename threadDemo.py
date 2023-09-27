import threading
import time

print('Start of Program.')

def takeaNap():
    time.sleep(5)
    print('Wake up.')

threadObj = threading.Thread(target=takeaNap)
threadObj.start()

print('End of Program.')
