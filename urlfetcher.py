from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

def getURLs(userId, appId):

    sharedFilesList = []
    newAdded = True
    currPage = 1
    print("Searching for screenshots")
    while(newAdded):
        newAdded = False
        urlString = "https://steamcommunity.com/id/" + userId + "/screenshots/?p=" + str(currPage) + "&appid=" + str(appId) + "&sort=newestfirst&browsefilter=myfiles&view=imagewall"
        
        url = urllib.request.urlopen(urlString)
        soup = BeautifulSoup(url, "html.parser")
        for hyperlink in soup.findAll('a'):
            parse = urlparse(hyperlink.get("href"))
            if (parse.path == "/sharedfiles/filedetails/" and hyperlink.get("href") not in sharedFilesList):
                newAdded = True
                sharedFilesList.append(hyperlink.get("href"))
        currPage = currPage + 1
    return sharedFilesList
    

def dumpURLs(sharedFilesList):
    print ("Dumping URLs to file")
    with open ('idlist.txt', 'w') as fp:
        fp.writelines("%s\n" % item for item in sharedFilesList)
