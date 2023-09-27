# Write your code here :-)
#!python3
#phoneAndEmail.py - finds phone numbers and email addresses on thre clipboard
import pyperclip,re
phoneRegex=re.compile(r'''(
(\d{3}|\(\d{3}\))?       #areacode
(\s|-|\.)?               #separator
(\d{3})                 #first 3
(\s|-|\.)                #separator
(\d{4})               #last 4
(\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''',re.VERBOSE)


#TODO create email regex
emailRegex=re.compile(r'''(
([a-zA-Z+-.0-9%_!#$&^*])+#username
(@)                      #@ symbol
([a-zA-Z0-9.-])          #domain name
(\.[a-zA-Z]{2,4})       #.something
)''',re.VERBOSE)
#TODO find matches in clipboard text
text=str(pyperclip.paste())
print(text)
matches=[]
for group in phoneRegex.findall(text):
    print(matches)
    phoneNum = '-'.join([group[1],group[3],group[5]])
    if group[6]!='':
        phoneNum+=' x'+group[6]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])
#TODO copy results to the clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard.')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

