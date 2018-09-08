import mainCache
import maze


class Main:

    __cache = None

    def __init__(self):
        Main.__cache = mainCache.cache.Cache()


    def getCache(self):
        return self.__cache


def playIntro(intro):
    count = 0
    for item in intro:
        if count != 0:
            input("Press Enter to continue...")
        count+=1
        print(item)



def playClimax(climax):
    count = 0
    print("\n")
    for item in climax:
        if count != 0:
            input("Press Enter to continue...")
        count+=1
        print(item)

def getQuestionFromCache(searchValue):
    mainObj = Main()
    cache = Main.getCache(mainObj)
    questions = cache.getQuestions()
    for item in questions:
        if item['id'] == searchValue:
            return item
    return None


def displayQuestion(question):
    print("\n")
    print(question['Q'])
    options = question['O']
    for item in options:
        print(item)
    print("\n")


def getAnswer():
    answer = input("What should I do?? : ")
    valid = ['A','B','C','D']
    if answer in valid:
        return answer
    else:
        print("Invalid option, please try again.")
        return getAnswer()


def getNextQuestion(questionId, answer):
    mainObj = Main()
    cache = Main.getCache(mainObj)
    screenplay = cache.getScreenPlay()
    for item in screenplay:
        if item[0] == questionId:
            if item[1] == "<CLIMAX>" or item[2] == "<CLIMAX>":
                climax = cache.getClimax()
                playClimax(climax)
                return None
            if item[1] == answer:
                return item[2]
    return None


def playQuestions(questionId):
    question = getQuestionFromCache(questionId)
    if question != None:
        displayQuestion(question)
        answer = getAnswer()
        nextQuestionId = getNextQuestion(questionId,answer)
        if nextQuestionId != None:
            playQuestions(nextQuestionId)


def playMaze():
    maze.startMaze()


def start():
    mainObj = Main()
    print("\n")
    cache = Main.getCache(mainObj)
    for item in cache.getScreenPlay():
        if item == "<INTRO>":
            intro = cache.getIntro()
            playIntro(intro)
        elif item == "<MAZE>":
            playMaze()
        else:
            playQuestions(item[0])
            break

start()
    






