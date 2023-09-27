# Write your code here :-)
def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,2):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,6):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,11):
        if not text[i].isdecimal():
            return False
    return True

message='Call me at 415-999-6565 tomorrow. 415-868-7777 is my office.'
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+chunk)
print('Done')
