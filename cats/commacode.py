def comcode(listt):
    if len(listt)>1:
        l=''
        for i in range(len(listt)-1):
            l=l+str(listt[i])+','
        l=l+' and '+str(listt[-1])
        return str(l)
    elif len(listt)==1:
        return str(listt[0])
    else:
        return ''

spam=['Hello']
print(comcode(spam))
