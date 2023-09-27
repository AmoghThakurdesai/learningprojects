import datetime
import time
#2022/6/15
theoAtt={'EM2':[20,23],'CHEM':[21,27],'BXE':[21,23],'PPS':[23,30],'EG':[16,19],'ES2':[7,9], 'CS':[12,13]}
pracAtt={'EM2':[7,8],'CHEM':[7,7],'BXE':[5,5],'PPS':[5,6],'EG':[5,7],'CAD':[7,8], 'PBL':[7,14]}
def attCalc(dict):
    a, c = 0,0
    for value in dict.values():
       a += value[0]
       c += value[1]
    return str(a/c*100)+' %',datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

print(f'Theory attendance: {attCalc(theoAtt)}')
print(f'Prac attendance: {attCalc(pracAtt)}')
filename=f'attendance{time.time()}.txt'
logfile=open(filename,'w')
logfile.write(f'Theory attendance: {attCalc(theoAtt)}')
logfile.write('\n')
logfile.write(f'Prac attendance: {attCalc(pracAtt)}')
logfile.close()



