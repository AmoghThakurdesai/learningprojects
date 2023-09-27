# make a notepad file before doing this
import time

import pyautogui as pag
import pyperclip

print('Wait 3 seconds for cursor to move to seleted text')
time.sleep(3)

pag.click()
pag.hotkey('ctrl', 'a')
pag.hotkey('ctrl', 'c')

text = pyperclip.paste()

pag.hotkey('ctrl', 'v')
print(text)





