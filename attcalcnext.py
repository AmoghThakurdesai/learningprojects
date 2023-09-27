import time

import attcalc
import datetime

# input list for attendance in (theory list,practical list format)
# use 'EM2
theo=attcalc.theoAtt
pract=attcalc.pracAtt
def attnext(theory, pracs,absenttheory,absentpracs):
    for lec in theory:
        theo[lec][0]+=1
        theo[lec][1]+=1
    for prac in pracs:
        pract[prac][0]+=1
        pract[prac][1]+=1
    for abth in absenttheory:
        theo[abth][1]+=1
    for abpr in absentpracs:
        pract[abpr][1]+=1
    return attcalc.attCalc(theo),attcalc.attCalc(pract)
print(attnext(['PPS','EM2','BXE','CHEM','CS','EM2','BXE','ES2','BXE','ES2','CHEM','PPS','EM2'],['PBL','PBL','EG','PPS','CHEM','PBL'],[],[]))
print(theo,pract)
filename=f'attendance next {time.time()}.txt'
logfile=open(filename,'w')
logfile.write(attcalc.attCalc(theo)[0])
logfile.write('\n')
logfile.write(attcalc.attCalc(pract)[0])
logfile.write('\n')
logfile.write(str(theo))
logfile.write('\n')
logfile.write(str(pract))
logfile.write('\n')
logfile.write(datetime.datetime.now().strftime("%d%m%Y %H%M%S"))