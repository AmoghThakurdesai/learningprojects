# Write your code here :-)
#!python3
#selectcopy.py - copies selectively based on file extensions
#insert path of folder in function
import os,shutil,re
from pathlib import Path

def fileExtractor(extension,folder):
    p=Path.cwd()

    extractFilesRegex=re.compile(r'extracted(\s)files(\s)(\d)')
    m=[]
    for i in os.listdir():
        if extractFilesRegex.findall(i)!=[]:
            m.append(i)
    os.mkdir(p/f'extracted files {len(m)+1}')
    ext=Path(p/f'extracted files {len(m)+1}')


    for foldername,subfolders,filenames in os.walk(folder):
        print(f'Searching {foldername}....')
        absWorkDir=os.path.abspath(foldername)
        for filename in filenames:
            t=os.path.join(absWorkDir,filename)
            try:
                if os.path.basename(t).endswith(extension) :
                    print(f'Copying {Path(filename)}.....')
                    shutil.copy(t,ext)
            except shutil.SameFileError:
                break
    print('Done')

fileExtractor('.py','D:\PythonFiles')

