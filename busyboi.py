import pyautogui as pag
pag.click()
t=0
TIME = 500
while t < TIME:
    pag.move(200,200)
    pag.sleep(10)
    t += 10


