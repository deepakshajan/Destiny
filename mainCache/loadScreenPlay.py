import mainCache.cache as cache

def readScreenPlayFile():
    file = open("./conf/screenplay.txt")
    screenPlay = []
    for line in file:
        if "<INTRO>" in line:
            screenPlay.append(line.replace("\n",""))
        elif "<MAZE>" in line:
            screenPlay.append(line.replace("\n",""))
        else:
            line = line.split(".")
            question = []
            for lineItem in line:
                question.append(lineItem.replace("\n",""))
            screenPlay.append(question)
    return screenPlay



class LoadScreenPlay:

    def __init__(self):
        fileContent = readScreenPlayFile()
        cacheObj = cache.Cache()
        for item in fileContent:
            cacheObj.addToScreenPlay(item)
