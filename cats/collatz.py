# Write your code here :-)

def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1
while True:
    print('Type a number for the Collatz sequence')
    try:
        num=int(input())
        while num!=1:
            num=collatz(int(num))
    except ValueError:
        print('')
