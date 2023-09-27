# Write your code here :-)
#! python3
# showbig - show what big files there are
# filesize limit in mb
import os


def showbig(folder,sizelimit):
    for foldername,subfolders,filenames in os.walk(folder):
        absWorkDir=os.path.abspath(foldername)

        for filename in filenames:
            t=os.path.join(absWorkDir,filename)
            current=os.path.getsize(t)
            if current>sizelimit*1024*1024:
                print(f'Found big file {t}, size {current/1024/1024} MB')

showbig('D:/Epic Launcher',100)
