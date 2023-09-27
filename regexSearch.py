# Write your code here :-)
#opens all text files in folder
import re
from pathlib import Path
p=Path('C:/Users/amogh/Desktop')
regex=input('Enter your regex(no quotes):')
matches=[]
userRegex=re.compile('%s'% regex)
for file in list(p.glob('*.txt')):
    filecontent=''.join(file.read_text())

    #search for any line which matches regex
    matches+=userRegex.findall(str(filecontent))

#print results to screen
print(matches)
print(len(matches))
