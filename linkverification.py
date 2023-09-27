# Write your code here :-)
import requests,bs4


def dldlinkedpage(url):
    res=requests.get(url)
    res.raise_for_status
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
        tempurl=link.get('href')
        finalurl=''
        err=[]
        if tempurl==None:
            continue
        elif tempurl.startswith('/'):
            finalurl=url+tempurl
        elif tempurl.startswith('https:'):
            finalurl=tempurl
        elif tempurl.startswith('#'):
            finalurl=url+tempurl
        res=requests.get(finalurl)
        if res.status_code==404:
            print(finalurl+' is giving 404 error.')

dldlinkedpage('https://en.wikipedia.org/wiki/India')
