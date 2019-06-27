from tkinter import *
import tkinter
from tkinter import ttk
from EnigmaController import EnigmaController
Keyboard_App = tkinter.Tk()

buttons = [
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M',
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

plainText = Text(Keyboard_App, width=80, height=1, state='disabled')
plainText.grid(row=1, columnspan=20)
label1 = tkinter.Label(Keyboard_App, text="Texto Plano:")
label1.grid(row=1, columnspan=1)
label2 = tkinter.Label(Keyboard_App, text="Texto Cifrado:")
label2.grid(row=2, columnspan=1)
cipherText = Text(Keyboard_App, width=80, height=1, state='disabled')
cipherText.grid(row=2, columnspan=20)

machine = EnigmaController(['I', 'II', 'III'], ['A', 'D', 'U'],'b')


def deleteText(object):
    object.configure(state='normal')
    object.delete('1.0',tkinter.END)
    object.configure(state='disabled')


def insertAtStart(object, value):
    object.configure(state='normal')
    object.delete('1.0',tkinter.END)
    object.insert('1.0', value)
    object.configure(state='disabled')


def buttonReset():
    machine.resetKeys()
    [l, m, r] = machine.getKey()
    insertAtStart(keyTextL, l)
    insertAtStart(keyTextM, m)
    insertAtStart(keyTextR, r)
    deleteText(plainText)
    deleteText(cipherText)


reset = tkinter.Button(Keyboard_App, text='RESET KEYS', width=7, bg="#000000", fg="#ffffff", highlightthickness=4, padx=12,
                       pady=4, activebackground="#000000", activeforeground="#ffffff", bd=4, command=buttonReset)
reset.grid(row=0, column=5)

insertAtStart(keyTextL, 'A')
insertAtStart(keyTextM, 'D')
insertAtStart(keyTextR, 'U')
varRow = 3
varColumn = 0


def configuration():
    win = tkinter.Toplevel()
    win.wm_title("Configuración de Enigma")

    l = tkinter.Label(win, text="Llaves (A a Z)")
    l.grid(row=0, column=0)

    d = tkinter.Label(win, text="Rotores (I, II, ..., V)")
    d.grid(row=1, column=0)

    labelLK = tkinter.Label(win, text="Izq")
    labelLK.grid(row=0, column=1)
    keyTextLK = Text(win, width=3, height=1)
    keyTextLK.grid(row=0, column=1,padx=(100,10))

    labelMK = tkinter.Label(win, text="Med")
    labelMK.grid(row=0, column=2)
    keyTextMK = Text(win, width=3, height=1)
    keyTextMK.grid(row=0, column=2,padx=(100,10))

    labelRK = tkinter.Label(win, text="Der")
    labelRK.grid(row=0, column=3)
    keyTextRK = Text(win, width=3, height=1)
    keyTextRK.grid(row=0, column=3,padx=(100,10))

    labelLR = tkinter.Label(win, text="Izq")
    labelLR.grid(row=1, column=1)
    keyTextLR = Text(win, width=3, height=1)
    keyTextLR.grid(row=1, column=1,padx=(100,10))

    labelMR = tkinter.Label(win, text="Med")
    labelMR.grid(row=1, column=2)
    keyTextMR = Text(win, width=3, height=1)
    keyTextMR.grid(row=1, column=2,padx=(100,10))

    labelRR = tkinter.Label(win, text="Der")
    labelRR.grid(row=1, column=3)
    keyTextRR = Text(win, width=3, height=1)
    keyTextRR.grid(row=1, column=3,padx=(100,10))

    a = ttk.Button(win, text="Aplicar", command=win.destroy)
    a.grid(row=3, column=1,pady=(10,10))

    b = ttk.Button(win, text="Cancelar", command=win.destroy)
    b.grid(row=3, column=2,pady=(10,10))


config = tkinter.Button(Keyboard_App, text='Config', width=7, bg="#000000", fg="#ffffff", highlightthickness=4, padx=12,
                       pady=4, activebackground="#000000", activeforeground="#ffffff", bd=4, command=configuration)
config.grid(row=0, column=7)


def keypress(event):
    event.char = event.char.upper()
    if event.char in buttons:
        insert(plainText, event.char)
        try:
            if event.char == ' ':
                insert(cipherText, ' ')
            else:
                cipher = enigmify(event.char.lower())
                cipher = cipher.upper()
                buttonL[cipher].configure(highlightbackground='red')
                buttonL[cipher].after(1000, lambda: buttonL[cipher].configure(highlightbackground='#d9d9d9'))
                insert(cipherText, cipher)
        except KeyError:
            print('Key outside enigma!')


def insert(object, value):
    object.configure(state='normal')
    object.insert(tkinter.END, value)
    object.configure(state='disabled')


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
    if button == 'P' or button == 'M' or button =='L':
        varColumn = 0
        varRow += 1

Keyboard_App.title("La maquina Enigma (version digital)")
Keyboard_App.bind('<Key>', keypress)
Keyboard_App.mainloop()
