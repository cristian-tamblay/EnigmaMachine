from Plugboard import Plugboard
import random
random.seed(1000)

plug = Plugboard()
print(plug.cipher(2))

text='FVPJIAOYEDRZXWGCTKUQSBNMHL'.lower()
perm = []
for char in text:
    perm.append(ord(char) - 96)

print(perm)