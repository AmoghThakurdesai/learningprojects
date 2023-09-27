# Write your code here :-)
#! python 3
#fillinggaps-filling in the gaps for files with a given prefix
#insert path of folder in function
import re,os,shutil
def fillthegaps(folder,prefix):
    #find all files with a given prefix
    prefixRegex=re.compile(r'(^%s)(\d+).(.*$)'% prefix)
    workingDir=os.path.abspath(folder)
    prefixfiles=[]
    for foldername,subfolders,filenames in os.walk(folder):
        absWorkDir=os.path.abspath(foldername)
        for filename in filenames:
            if len(prefixRegex.findall(filename))!=0:
                prefixfiles.append(filename)
    #locate the gaps
    gapnum=[]
    for i in range(len(prefixfiles)-1):
        try:
            num1=prefixRegex.search(prefixfiles[i]).group(2)
            num2=prefixRegex.search(prefixfiles[i+1]).group(2)
            if int(num1)+1==int(num2):
                continue
            else:
                print(f'Gap between {prefixfiles[i]} and {prefixfiles[i+1]}.')
                gapnum.append(i)
        except IndexError:
            break


    #rename the later files

    for filename in prefixfiles:
        try:
            oldfilename=os.path.join(folder,filename)
            newname=prefix+'0'*(len(prefixRegex.search(prefixfiles[-1]).group(2))-len(str(prefixfiles.index(filename)+1)))+str(prefixfiles.index(filename)+1)+'.'+prefixRegex.search(filename).group(3)
            newfilename=os.path.join(folder,newname)

            shutil.copy(oldfilename,newfilename)
        except shutil.SameFileError:
            continue


fillthegaps('D:\PythonFiles\Capitals Quizzes Txt','capitalsquiz_answers')

def addgaps(folder,prefix,gapnum):
    #gapnum is number after which you want a gap
    #find all files with a given prefix
    prefixRegex=re.compile(r'(^%s)(\d+).(.*$)'% prefix)
    workingDir=os.path.abspath(folder)
    prefixfiles=[]
    for foldername,subfolders,filenames in os.walk(folder):
        absWorkDir=os.path.abspath(foldername)
        for filename in filenames:
            if len(prefixRegex.findall(filename))!=0:
                prefixfiles.append(filename)
    #add the gaps
    for i in range(len(prefixfiles),gapnum-1,-1):
        try:
            oldfilename=os.path.join(folder,prefixfiles[i])
            newname=prefix+'0'*(len(prefixRegex.search(prefixfiles[-1]).group(2))-len(str(int(prefixRegex.search(prefixfiles[i]).group(2))+1)))+str(int(prefixRegex.search(prefixfiles[i]).group(2))+1)+'.'+prefixRegex.search(prefixfiles[i]).group(3)
            newfilename=os.path.join(folder,newname)
            print(f'Renaming {oldfilename} to {newname}')
            os.rename(oldfilename,newfilename)
        except IndexError:
            continue
addgaps('D:\PythonFiles\Capitals Quizzes Txt','capitalsquiz_answers',19)

