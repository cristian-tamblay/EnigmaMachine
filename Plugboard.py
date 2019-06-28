class Plugboard:
    def __init__(self):
        self.permutation = list(range(0, 27)) # Plugboard conectado directamente

    def cipher(self, plainLetter):
        return self.permutation[plainLetter]
