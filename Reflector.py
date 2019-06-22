import random

class Plugboard:
    def __init__(self, reflectorId):
        self.reflectors = dict()
        self.reflectors['b'] = [0, 25, 18, 21, 8, 17, 19, 12, 4, 16, 24, 14, 7, 15, 11, 13, 9, 5, 2, 6, 26, 3, 23, 22, 10, 1, 20]
        self.reflectors['c'] = [0, 6, 22, 16, 10, 9, 1, 15, 25, 5, 4, 18, 26, 24, 23, 7, 3, 20, 11, 21, 17, 19, 2, 14, 13, 8, 12]
        self.chosenReflector = self.reflectors[reflectorId]

    def cipher(self, plainLetter):
        return self.chosenReflector[plainLetter]

