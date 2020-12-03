import idfetcher
from urllib.parse import urlunsplit
from urllib.parse import urlparse
from urllib.parse import urlunparse
import urllib.request
from bs4 import BeautifulSoup

idlist=[]
idlist = idfetcher.getIDs()
iterator = 0
print('Fetched IDs!')
print (idlist)
parsed = list(urlparse('https://steamcommunity.com/sharedfiles/filedetails/?id=1481162777'))
for id in idlist:
    #print(id)
    #print(parsed)
    parsed[4] = id
    screenshotcontainer = urlunparse(parsed)
    #print(screenshot)
    htmlfile = urllib.request.urlopen(screenshotcontainer)
    soup = BeautifulSoup(htmlfile, 'html.parser')
    for link in soup.find_all('a'):
        parsed2 = urlparse(link.get('href'))
        if parsed2.netloc=='steamuserimages-a.akamaihd.net':
            try:
                #print(parsed2)
                truescreenshoturl=urlunparse(list(parsed2))
                screenshotresponse = urllib.request.urlopen(truescreenshoturl)
                screenshotdata = screenshotresponse.read()
                filename = 'file' +str(iterator)+ '.jpg'
                myfile = open(filename, 'wb')
                myfile.write(screenshotdata)
                myfile.close()
                iterator = iterator + 1
                print ('Saved ' + truescreenshoturl)
            except urllib.error.HTTPError as err:
                if err.code == 504:
                    print('504 encountered" ' + truescreenshoturl)
                    iterator = iterator + 1
                    continue
                else:
                    raise
            
    
    
    
