# bruteforce password breaker
import sys,PyPDF2
from pathlib import Path
dicfile=open('D://PythonFiles//dictionary.txt')
diclist=dicfile.readlines()
d=len(diclist)
file='encryptedminutes.pdf'#sys.argv[0]
for i in range(0,d):
    diclist.append(diclist[i].lower())
for j in range(0,len(diclist)-1):
    pdfReader=PyPDF2.PdfFileReader(file,'rb')
    success=pdfReader.decrypt(diclist[j][:-1])
    if success==1:
        print(diclist[j][:-1])
        break
    else:
        continue



