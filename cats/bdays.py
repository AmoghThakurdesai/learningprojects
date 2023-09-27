# Write your code here :-)
birthdays={'Ali':'April 1','Bob':'July 7','Cat':'Feb 29'}
while True:
    print('Enter a name:(blank to quit)')
    name = input()
    if name=='':
        break

    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name )
    else:
        print(' I donot have birthday information for '+name)
        print('What is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday database updated.')
