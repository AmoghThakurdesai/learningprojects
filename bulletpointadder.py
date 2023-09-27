# Write your code here :-)
#python3
#bulletptadder- adds wikipedia bullet pointd to the starts
#of eash line of text copied to the clipboard

import pyperclip
text= pyperclip.paste()

#Separate lines and add stars
lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)

pyperclip.copy(text)
