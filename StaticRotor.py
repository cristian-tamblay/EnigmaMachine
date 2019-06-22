class StaticRotor:
    def __init__(self):
        self.permutation = list(range(0, 27)) # Identidad

    def cipher(self, plainLetter):
        return self.permutation[plainLetter]
