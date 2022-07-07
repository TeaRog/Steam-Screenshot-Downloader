from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

def getURLs(userId, appId, page):
    print("    Searching for Screenshots Batch...")
    sharedFilesList = []
    newAdded = True
    
    while(newAdded):
        newAdded = False
        urlString = "https://steamcommunity.com/profiles/"+str(userId)+"/screenshots/?p="+str(page)+"&appid="+str(appId)+"&sort=oldestfirst&browsefilter=myfiles&view=grid"
        url = urllib.request.urlopen(urlString)
        soup = BeautifulSoup(url, "html.parser")

        for hyperlink in soup.findAll('a'):
            parse = urlparse(hyperlink.get("href"))
            if (parse.path == "/sharedfiles/filedetails/" and hyperlink.get("href") not in sharedFilesList):
                newAdded = True
                sharedFilesList.append(hyperlink.get("href"))

    return sharedFilesList

def dumpURLs(sharedFilesList):
    with open ('idlist.txt', 'w') as fp:
        fp.writelines("%s\n" % item for item in sharedFilesList)