import random


class Plugboard:
    def __init__(self):
        self.permutation = [-1] * 26
        letters = list(range(0, 26))  # 26 letras
        for i in range(0, 26):
            if self.permutation[i] == -1:
                keepLetter = random.random()
                if (keepLetter < 0.05 and i in letters) or len(letters) == 1:
                    self.permutation[i] = i
                    letters.remove(i)
                else:
                    letter = random.randint(1, len(letters) - 1)
                    self.permutation[i] = letters[letter]
                    self.permutation[letters[letter]] = i
                    letters.remove(letters[letter])
                    letters.remove(i)
        print(self.permutation)

    def cipher(self, plainLetter):
        return self.permutation[plainLetter]
