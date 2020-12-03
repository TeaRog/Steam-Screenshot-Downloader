from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

def getIDs():
    userID = "combatperson7"
    appId = 0

    sharedFilesList = []
    newAdded = True
    currPage = 1
    print("Searching for screenshots")
    while(newAdded):
        newAdded = False
        urlString = "https://steamcommunity.com/id/" + userID + "/screenshots/?p=" + str(currPage) + "&appid=" + str(appId) + "&sort=newestfirst&browsefilter=myfiles&view=imagewall"
        
        url = urllib.request.urlopen(urlString)
        soup = BeautifulSoup(url, "html.parser")
        for hyperlink in soup.findAll('a'):
            parse = urlparse(hyperlink.get("href"))
            if (parse.path == "/sharedfiles/filedetails/" and hyperlink.get("href") not in sharedFilesList):
                newAdded = True
                sharedFilesList.append(hyperlink.get("href"))
        currPage = currPage + 1
    print(currPage)
    
    print ("Dumping URLs to file")
    with open ('idlist.txt', 'w') as fp:
        fp.writelines("%s\n" % item for item in sharedFilesList)


    """
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
    """
getIDs()