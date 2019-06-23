from EnigmaController import EnigmaController
import random

random.seed(1000)

rotor = EnigmaController(['I', 'II', 'III'], ['A', 'D', 'U'],'b')
print(chr(rotor.cipher(0)+97))
print(chr(rotor.cipher(0)+97))
print(chr(rotor.cipher(0)+97))
print(chr(rotor.cipher(0)+97))