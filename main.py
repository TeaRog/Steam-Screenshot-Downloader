import urlfetcher
import downloader
from multiprocessing import Manager, Pool


if __name__ == '__main__':

    userId = "combatperson7"
    appId = 0

    sharedUrls = urlfetcher.getURLs(userId, appId)
    urlfetcher.dumpURLs(sharedUrls)

    print("Downloading images")
    pool = Pool(processes=6)
    results = pool.map(downloader.downloadImage, sharedUrls)
    pool.close()
    pool.join()

    screenshotDataDict = {}
    for id, img in results:
        screenshotDataDict[id] = img


    downloader.writeImages(screenshotDataDict)








