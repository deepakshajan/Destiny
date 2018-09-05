class Cache:
    'Caches the values needed for the application.'

    __intro = []
    __climax = []
    __questions = []
    __screenplay = []

    def addToIntro(self,value:[]):
        self.__intro.append(value)

    def addToClimax(self,value:[]):
        self.__climax.append(value)

    def addToQuestions(self,value:[]):
        self.__questions.append(value)

    def addToScreenPlay(self,value:[]):
        self.__screenplay.append(value)

    def getIntro(self):
        return self.__intro

    def getClimax(self):
        return self.__climax

    def getQuestions(self):
        return self.__questions

    def getScreenPlay(self):
        return self.__screenplay

