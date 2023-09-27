#! python3
#threadedDownloadXkcd - Downloads xkcd comics using multiple threads

import os
import threading

import bs4
import requests

os.makedirs('xkcd',exist_ok=True)   #store comics in ./xkcd
def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        #Download the page
        print(f'Downloading page https://xkcd.com/{urlNumber}....')
        res=requests.get(f'https://xkcd.com/{urlNumber}')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text,'html.parser')

        #Find url of the comic image
        comicElem = soup.select('#comic img')
        if comicElem==[]:
            print('Could not find comic image.')
        else:
            comicUrl=comicElem[0].get('src')
            #Download the image
            print(f'Downloading image {comicUrl}')
            res=requests.get('https:'+comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
#TODO: Create and start the Thread objects
downloadThreads=[]
for i in range(0,2610,10):
    start=i
    end=i+9
    if start == 0:
        start=1#there is no comic 0 so set it to 1
    downloadThread=threading.Thread(target=downloadXkcd,args=(start,end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
#TODO: Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')