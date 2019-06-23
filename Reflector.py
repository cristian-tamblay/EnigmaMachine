import random

class Reflector:
    def __init__(self, reflectorId):
        self.reflectors = dict()
        self.reflectors['b'] = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
        self.reflectors['c'] = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]
        self.chosenReflector = self.reflectors[reflectorId]

    def cipher(self, plainLetter):
        return self.chosenReflector[plainLetter]

