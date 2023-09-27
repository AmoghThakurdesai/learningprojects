# Write your code here :-)
def spam():
    global eggs
    eggs='spam' #this is the global

def bacon():
    eggs='bacon'#local

def ham():
    print(eggs)#global

eggs=42#global
spam()
print(eggs)
