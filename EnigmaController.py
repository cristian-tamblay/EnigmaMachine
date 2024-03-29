from Rotor import Rotor
from Plugboard import Plugboard
from StaticRotor import StaticRotor
from Reflector import Reflector


class EnigmaController:
    def __init__(self, rotors, keys, reflector):
        self.plug = Plugboard()
        self.static = StaticRotor()
        self.left = Rotor(rotors[0], keys[0])
        self.middle = Rotor(rotors[1], keys[1])
        self.right = Rotor(rotors[2], keys[2])
        self.reflector = Reflector(reflector)
        self.rotors = rotors
        self.initialKeys = keys

    def cipher(self, plainLetter):
        # Movimientos en notch/al iniciar cifrado
        if self.middle.isNotch():
            self.middle.step()
            self.left.step()
        if self.right.isNotch():
            if not self.middle.isNotch():
                self.middle.step()
        self.right.step()
        # Si se quiere usar el plugboard descomentar las siguientes lineas
        cipherPlug = self.plug.cipher(plainLetter)
        cipherStatic = self.static.cipher(cipherPlug)
        cipherRightRotor = self.right.cipherLeft(cipherStatic)
        cipherMiddle = self.middle.cipherLeft(cipherRightRotor)
        cipherLeft = self.left.cipherLeft(cipherMiddle)
        cipherReflector = self.reflector.cipher(cipherLeft)
        cipherLeft = self.left.cipherRight(cipherReflector)
        cipherMiddle = self.middle.cipherRight(cipherLeft)
        cipherRight = self.right.cipherRight(cipherMiddle)
        return cipherRight

    def getKey(self):
        return [self.left.getKey(), self.middle.getKey(), self.right.getKey()]

    def getRotors(self):
        return [self.left.getRotor(), self.middle.getRotor(), self.right.getRotor()]

    def setRotorsAndKeys(self, rotors,keys):
        self.left = Rotor(rotors[0], keys[0])
        self.middle = Rotor(rotors[1], keys[1])
        self.right = Rotor(rotors[2], keys[2])
        self.initialKeys = keys

    def setKeys(self, keys):
        self.setRotorsAndKeys(self.rotors, keys)

    def resetKeys(self):
        self.setKeys(self.initialKeys)
