# Write your code here :-)# Write your code here :-)
import re
madlibRegex=re.compile(r'ADJECTIVE|VERB|NOUN|ADVERB')
textfile=open('madlibsfile.txt','r')
content=textfile.read()
textfile.close()
print(content)
matches=madlibRegex.findall(content)
for group in matches:
    def gramm():
        if group=='ADJECTIVE':
            return 'an adjective'
        elif group=='NOUN':
            return 'a noun'
        elif group=='ADVERB':
            return 'an adverb'
        elif group=='VERB':
            return 'a verb'
    rep=input('Enter '+gramm()+':\n')
    content=content.replace(group,rep,1)

print(content)
newfile=open('madlibsnew.txt','a+')
newfile.write(content)
newfile.close()
