# Write your code here :-)
import requests,bs4,re

def dldlinkedpage(url):
    res=requests.get(url)
    res.raise_for_status
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    siteRegex=re.compile(r'^https:\/\/([a-z0-9.]+)(.*)')
    baseurl='https://'+siteRegex.search(url).group(1)
    for link in soup.find_all('a'):
        tempurl=link.get('href')

        if tempurl==None:
            permurl=baseurl
        elif tempurl.startswith('#'):
            permurl=url+tempurl
        elif tempurl.startswith('https:'):
            permurl=tempurl
        elif tempurl.startswith('/'):
            permurl=baseurl
        elif tempurl.startswith('.'):
            permurl=baseurl+tempurl[1:]
        site=requests.get(permurl)
        print(permurl)
        err=[]
        if site.status_code==404:
            err.append(permurl)
    for i in err:
        print('Error for %s'%i)
dldlinkedpage('https://blog.hubspot.com/customers/404-pages-to-make-your-brand-stand-out')
