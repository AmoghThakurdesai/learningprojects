# Write your code here :-)
import random

number_of_streaks=0
streak=0
for x in range(10000):
    randoht=[]
    for i in range(100):
        randoht.append(random.randint(0 , 1))
    for i in range(1,len(randoht)):
        if randoht[i]==randoht[i-1]:
            streak+=1
        else:
            streak=1
        if streak==6:
            number_of_streaks+=1
            break
print(number_of_streaks)
print('Probablity of streak = '+str(number_of_streaks/10000))
