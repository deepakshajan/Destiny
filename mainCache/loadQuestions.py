import mainCache.cache as cache

def readQuestionsFile()->[]:
    file = open("./conf/questions.txt")
    questionList = []
    questionItem = {}
    optionList = []
    for line in file:
        if "===" not in line:
            lineList = line.split("~")
            if lineList[0]=="Q":
                if questionItem:
                    questionItem["O"] = optionList
                    questionList.append(questionItem)
                questionItem = {}
                optionList = []
                questionItem["id"] = lineList[1]
                questionItem["Q"] = lineList[2].replace("\n","")
            elif lineList[0]=="O":
                optionList.append(lineList[1].replace("\n",""))
            else:
                questionItem["Q"] += lineList[0].replace("\n","")
    questionItem["O"] = optionList
    questionList.append(questionItem)
    return questionList



class LoadQuestions:

    def __init__(self):
        fileContent = readQuestionsFile()
        cacheObj = cache.Cache()
        for item in fileContent:
            cacheObj.addToQuestions(item)
