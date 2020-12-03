from urllib.parse import urlparse
from urllib.parse import parse_qs
import os.path
from multiprocessing import Manager, Pool

import urllib.request
from bs4 import BeautifulSoup


def writeImages(screenshotDataDict):
    if not (os.path.exists("imgs")):
        os.mkdir("imgs")
    for key, value in screenshotDataDict.items():
        filename = str(key) + ".jpg"
        with open(os.path.join("imgs", filename), 'wb') as imgFile:
            imgFile.write(value)


def downloadImage(sharedFileUrl):
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
    return (id, screenshotData)