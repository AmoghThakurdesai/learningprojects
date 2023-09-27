# Write your code here :-)
myPets=['zophie','poooka','fattail']
print('enter a pet name:')
name=input()
if name not in myPets:
    print('i donot have a pet named '+ name)
else:
    print(name+'is my pet.')
