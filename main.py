import urlfetcher
import downloader

userId = "combatperson7"
appId = 0

sharedUrls = urlfetcher.getURLs(userId, appId)
urlfetcher.dumpURLs(sharedUrls)
#sharedUrls = ["https://steamcommunity.com/sharedfiles/filedetails/?id=2307100788"]
downloader.writeImages(downloader.downloadImages(sharedUrls))
