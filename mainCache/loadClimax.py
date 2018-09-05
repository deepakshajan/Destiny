import mainCache.cache as cache


def readClimaxFile()->[]:
    climaxFile = open('./conf/climax.txt','r')
    climaxSection = []
    climaxSectionFragment = ""
    for line in climaxFile:
        if "<PAUSE>" not in line:
            line = line.replace('\n','')
            climaxSectionFragment+=line
        else:
            climaxSection.append(climaxSectionFragment)
            climaxSectionFragment = ""
    climaxSection.append(climaxSectionFragment)
    return climaxSection

class Loadclimax:

    def __init__(self):
        fileContent = readClimaxFile()
        cacheObj = cache.Cache()
        for item in fileContent:
            cacheObj.addToClimax(item)
