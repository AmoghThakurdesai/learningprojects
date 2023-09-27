import time

import pyautogui as pag

time.sleep(5)
pag.click()
distance=300
change=20
while distance >0:
    distance = distance - change
    pag.drag(distance,0,duration=0.2)
    pag.drag(0,distance,duration=0.2)
    distance = distance - change
    pag.drag(-distance,0,duration=0.2)
    pag.drag(0,-distance,duration=0.2)
