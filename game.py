class Game:
    def __init__(self, word):
        self.word = word
        self.letters = []
        self.wrdLength = len(self.word)
        self.usedLetters = []

        self.health = 5
        self.win = 0

        for i in range(self.wrdLength):
            self.letters.append('_')

    def inputLetter(self):
        userInput = input("podal literke: ")
        self.checkIfLetter(userInput)
    
    def printUserLetters(self):
        output = ''

        for el in self.letters:
            output += el

        print(output)
    
    def winCheck(self):
        if '_' not in self.letters:
            print("wygrales!")
            self.win = 1


    def checkIfLetter(self, literka):
        flag = 0
        isLetterInWord = 0

        for i in self.usedLetters:
            if i == literka:
                print("Użyłeś już tej literki")
                return

        for i in range(self.wrdLength):
            if self.word[i] == literka:
                self.letters[i] = self.word[i]
                isLetterInWord = 1

                if flag == 0:
                    self.addUsedLetter(literka)
                    flag = 1
        
        if not isLetterInWord:
            self.health -= 1
            self.addUsedLetter(literka)
            print("Nie ma takiej literki")
            print("zostalo zyc: ", self.health)

            if not self.health:
                self.przegrana()
                return
                    
        self.winCheck()
        self.printUserLetters()


    def addUsedLetter(self, letter):
        self.usedLetters.append(letter)

    def printUsedLetters(self):
        output = ''

        for el in self.usedLetters:
            output += el

        print(output)

    def przegrana(self):
        print("Przegrales :c")
        self.win = 1
