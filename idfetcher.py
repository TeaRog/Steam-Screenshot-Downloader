from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import pickle
def getIDs():
    Templist=[]
    i=1
    for i in range(1,30):
        u2 = urllib.request.urlopen('https://steamcommunity.com/id/combatperson/screenshots?p=' + str(i) + '&sort=newestfirst&browsefilter=myfiles&view=grid&privacy=14')
        soup= BeautifulSoup(u2, 'html.parser')
        for link in soup.find_all('a'):
            #print(link.get('href'))
            parsed = urlparse(link.get('href'))
            if parsed.path == '/sharedfiles/filedetails/':
                Templist.append(parsed.query)
                print(parsed)
        i = i+1
    print ("Dumping ID's to file")
    with open ('idlist.txt', 'wb') as fp:
        pickle.dump(Templist,fp)
    return Templist
