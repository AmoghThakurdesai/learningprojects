import re
def strip(text,remove):
    if remove=='':
        stripspace=re.compile(r'^(\s*)(\S*)(\s*)$')
        return stripspace.search(text).group(2)

    else:
        removestart=re.compile(r'(^[%s]*)'%remove)
        removeend=re.compile(r'([%s]*$)'%remove)
        start=removestart.search(text)
        end=removeend.search(text)
        return text[len(start.group()):len(text)-len(end.group())]

usertext=input('Enter text you want to strip: ')
userremove=input('Enter the character u want stripped(space by default): ')
print(strip(usertext,userremove))

