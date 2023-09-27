# Write your code here :-)


def leapyear(y):
    if y%4!=0:
        return False
    elif y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        return True



print(leapyear(1900))
