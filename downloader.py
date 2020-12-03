from urllib.parse import urlparse
from urllib.parse import parse_qs
import os.path

import urllib.request
from bs4 import BeautifulSoup


def downloadImages(sharedFilesUrlList):
    print("Downloading images")
    screenshotDataDict = {}
    for sharedFileUrl in sharedFilesUrlList:
        #Open the sharedfiles page
        html = urllib.request.urlopen(sharedFileUrl)
        soup = BeautifulSoup(html, "html.parser")

        #Find the image and get its source/CDN url.
        hyperlink = soup.find(id="ActualMedia")
        CDNUrl = urlparse(hyperlink.get("src"))._replace(query=None).geturl()
        
        #Open the source url and read the image data
        screenshotURL = urllib.request.urlopen(CDNUrl)
        screenshotData = screenshotURL.read()

        #putting into a dict with the steam image id and the image data (its probably not a good idea to put the image data as a hashmap?)
        id = int(parse_qs(urlparse(sharedFileUrl).query)["id"][0])
        screenshotDataDict[id] = screenshotData

    return screenshotDataDict

def writeImages(screenshotDataDict):
    if not (os.path.exists("imgs")):
        os.mkdir("imgs")
    for key, value in screenshotDataDict.items():
        filename = str(key) + ".jpg"
        with open(os.path.join("imgs", filename), 'wb') as imgFile:
            imgFile.write(value)



"""
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
"""           
    
    
    
