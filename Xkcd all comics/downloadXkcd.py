#! python3
# downloadXkcd.py - downloads every xkcd comic

import requests,os,bs4

url='https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd
while not url.endswith('#'):
    #dowload the page
    print(f'Downloading page {url}...')

    #find the url of comic image
    res=responses.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text,'html.parser')
    #find url of comic image
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('Could not find comic image.')
    else:
        comicUrl='https:'+comicElem[0].get('src')
    #download the image
        print(f'Downloading image {comicUrl}......')
        res=requests.get(comicUrl)
        res.raise_for_status()
    #save the image to ./xkcd
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #get the prev buttons url
    prevLink=soup.select('a[rel="prev"]')[0]
    url='https://xkcd.com'+prevLink.get('href')

print('Done')
