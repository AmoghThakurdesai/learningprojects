# Write your code here :-)
import random,time,threading
print('MULTIPLICATION QUIZ')
numQ=10
correctans=0
for questionNumber in range(1,numQ+1):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    ans=num1*num2
    tries=0
    maxtries=3
    while tries<=maxtries:
        timer=threading.Timer(8,print,['Your time is up!'])
        timer.start()
        prompt='#%s:%sx%s='%(questionNumber,num1,num2)
        tries+=1
        response=input(prompt)
        timer.cancel()
        if response!='':
            if int(response)==ans:
                print('Correct!')
                correctans+=1
                break
            else:
                if tries==maxtries:
                    print('Out of tries')
                    break
                else:
                    print('Wrong answer!')
                    continue


    time.sleep(1)
print(correctans)
print('You score:%s/%s'%(correctans,numQ))

