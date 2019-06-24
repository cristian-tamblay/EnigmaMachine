from tkinter import *
import tkinter
from EnigmaController import EnigmaController
Keyboard_App = tkinter.Tk()

buttons = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
    ' ',
]

buttonL = {}
label0 = tkinter.Label(Keyboard_App, text="Llaves Rotores:")
label0.grid(row=0, columnspan=1)

labelL = tkinter.Label(Keyboard_App, text="Izq")
labelL.grid(row=0, column=1)
keyTextL = Text(Keyboard_App, width=2, height=1)
keyTextL.grid(row=0, column=1, columnspan=2)

labelM = tkinter.Label(Keyboard_App, text="Med")
labelM.grid(row=0, column=2)
keyTextM = Text(Keyboard_App, width=2, height=1)
keyTextM.grid(row=0, column=2, columnspan=2)

labelR = tkinter.Label(Keyboard_App, text="Der")
labelR.grid(row=0, column=3)
keyTextR = Text(Keyboard_App, width=2, height=1)
keyTextR.grid(row=0, column=3,columnspan=2)

plainText = Text(Keyboard_App, width=80, height=1)
plainText.grid(row=1, columnspan=20)
label1 = tkinter.Label(Keyboard_App, text="Texto Plano:")
label1.grid(row=1, columnspan=1)
label2 = tkinter.Label(Keyboard_App, text="Texto Cifrado:")
label2.grid(row=2, columnspan=1)
cipherText = Text(Keyboard_App, width=80, height=1)
cipherText.grid(row=2, columnspan=20)
machine = EnigmaController(['I', 'II', 'III'], ['A', 'D', 'U'],'b')
varRow = 3
varColumn = 0


def keypress(event):
    event.char = event.char.lower()
    if event.char in buttons:
        insert(plainText, event.char)
        try:
            if event.char == ' ':
                insert(cipherText, ' ')
            else:
                cipher = enigmify(event.char)
                buttonL[cipher].configure(highlightbackground='red')
                buttonL[cipher].after(1000, lambda: buttonL[cipher].configure(highlightbackground='#d9d9d9'))
                insert(cipherText, cipher)
        except KeyError:
            print('Key outside enigma!')


def insert(object, value):
    object.insert(tkinter.END, value)


def insertAtStart(object, value):
    object.delete('1.0',tkinter.END)
    object.insert('1.0', value)


def enigmify(value):
    cipher = chr(machine.cipher(ord(value)-97)+97)
    [l, m, r] = machine.getKey()
    insertAtStart(keyTextL, l)
    insertAtStart(keyTextM, m)
    insertAtStart(keyTextR, r)
    return cipher


for button in buttons:
    if button != " ":
        but = tkinter.Button(Keyboard_App, text=button, width=5, bg="#000000", fg="#ffffff", highlightthickness=4, padx=12,
                       pady=4, activebackground="#000000", activeforeground="#ffffff", bd=4)
        buttonL[button] = but
        but.grid(row=varRow, column=varColumn)

    if button == " ":
        but = tkinter.Button(Keyboard_App, text='Space', width=60, bg="#000000", fg="#ffffff", highlightthickness=4,
                        activebackground="#000000", activeforeground="#ffffff", padx=4, pady=4, bd=4)
        buttonL[' '] = but
        but.grid(row=7, columnspan=16)
    varColumn += 1
    if button == 'p' or button == 'l' or button =='m':
        varColumn = 0
        varRow += 1

Keyboard_App.title("La maquina Enigma (version digital)")
Keyboard_App.bind('<Key>', keypress)
Keyboard_App.mainloop()
