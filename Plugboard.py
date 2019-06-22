import random


class Plugboard:
    def __init__(self):
        self.permutation = [0]*27
        letters = list(range(1, 27)) # 26 letras
        for i in range(1,27):
            if self.permutation[i] == 0:
                keepLetter = random.random()
                if keepLetter < 0.05 and i in letters:
                    self.permutation[i] = i
                    letters.remove(i)
                else:
                    if len(letters) > 1:
                        letter = random.randint(1, len(letters)-1)
                    else:
                        letter = 0
                    self.permutation[i] = letters[letter]
                    self.permutation[letters[letter]] = i
                    letters.remove(letters[letter])
                    letters.remove(i)

    def cipher(self, plainLetter):
        return self.permutation[plainLetter]
