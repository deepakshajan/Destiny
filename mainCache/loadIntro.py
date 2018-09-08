import mainCache.cache as cache


def readIntroFile()->[]:
    introFile = open('./conf/intro.txt','r')
    introSection = []
    introSectionFragment = ""
    for line in introFile:
        if line.startswith("#") == False:
            if "<PAUSE>" not in line:
                line = line.replace('\n','')
                introSectionFragment+=line
            else:
                introSection.append(introSectionFragment)
                introSectionFragment = ""
    introSection.append(introSectionFragment)
    return introSection

class LoadIntro:

    def __init__(self):
        fileContent = readIntroFile()
        cacheObj = cache.Cache()
        for item in fileContent:
            cacheObj.addToIntro(item)
