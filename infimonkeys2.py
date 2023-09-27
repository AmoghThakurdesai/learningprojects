import random


def randlgenerator():
    letter = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '])
    return letter

def score(string):
    global solution
    solution = 'methinks it is like a weasel'
    score = 0
    for i in range(len(solution)):
        if string[i] == solution[i]:
            score += 1
    return score

def iterator(string1):
    t=0
    stringl=[]
    for i in string1:
        if i != solution[t]:
            stringl.append(randlgenerator())
        else:
            stringl.append(i)
        t += 1
    return ''.join(stringl)



def monkey():
    k=0
    tries = 0
    bestscore = 0
    string2 = ''.join([randlgenerator() for i in range(28)])
    for i in range(10000):
        string2 = iterator(string2)
        score1 = score(string2)
        if score1 == len(solution):
            print(f'Your monkey generated your string: {solution}')
            k += 1
        if score1 > bestscore:
            bestscore = score1
            print(string2)
        tries += 1
        if tries % 1000 == 0:
            print(bestscore)

solution = 'methinks it is like a weasel'
