class Rotor:
    def __init__(self, rotorId, key):
        self.rotors = dict()
        self.notchs = dict()
        self.rotors['I'] = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2,
                            9]
        self.notchs['I'] = 16

        self.rotors['II'] = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14,
                             4]
        self.notchs['II'] = 4

        self.rotors['III'] = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16,
                              14]
        self.notchs['III'] = 21

        self.rotors['IV'] = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22,
                             1]
        self.notchs['IV'] = 9

        self.rotors['V'] = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2,
                            10]
        self.notchs['V'] = 25

        self.chosenRotor = self.rotors[rotorId]
        self.chosenNotch = self.notchs[rotorId]

        self.keyValue = ord(key.lower()) - 97

        self.key = [(x + self.keyValue) % 26 for x in list(range(0, 26))]

    def cipherLeft(self, plainText):
        return (self.chosenRotor[self.key[plainText]] - self.keyValue) % 26

    def cipherRight(self, plainText):
        return (self.chosenRotor.index(self.key[plainText]) - self.keyValue) % 26

    def step(self):
        self.keyValue = (self.keyValue + 1) % 26
        self.key = [(x + self.keyValue) % 26 for x in list(range(0, 26))]

    def isNotch(self):
        return self.chosenNotch == self.keyValue

    def getKey(self):
        return chr(self.keyValue+97).upper()
