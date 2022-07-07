import urlfetcher
import downloader
from multiprocessing import Manager, Pool

def getImages(userId, appId, pageNum):
    sharedUrls = urlfetcher.getURLs(userId, appId, pageNum)
    urlfetcher.dumpURLs(sharedUrls)
    pool = Pool(processes=6)
    results = pool.map(downloader.downloadImage, sharedUrls)
    pool.close()
    pool.join()

    count = 0
    screenshotDataDict = {}
    
    for id, img in results:
        screenshotDataDict[id] = img
        count += 1

    downloader.writeImages(screenshotDataDict)

    return count

if __name__ == '__main__':

    userId = "CHANGE TO YOUR PERSONAL STEAM ACCOUNT ID"
    appId = 0 # specific game to download, 0 = all games
    
    page = 1 # leave unchanged

    print("Starting Steamcloud Screenshot Download: Account: "+str(userId))

    while True:# Do While Loop Emulation
        print("  Downloading Page "+str(page))

        count = getImages(userId, appId, page)
        print("    "+str(count) + " Images downloaded and saved to imgs folder")
        if count > 0:
            page+=1
        else:
            break