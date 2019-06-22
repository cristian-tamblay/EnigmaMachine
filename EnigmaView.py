from tkinter import *
import tkinter
Keyboard_App = tkinter.Tk()

buttons = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
    ' Space ',
]

buttonL = {}
plainText = Text(Keyboard_App, width=90, height=1)
plainText.grid(row=0, columnspan=15)
label1 = tkinter.Label(Keyboard_App, text="Texto Plano:")
label1.grid(row=0, columnspan=1)
label2 = tkinter.Label(Keyboard_App, text="Texto Cifrado:")
label2.grid(row=1, columnspan=1)
cipherText = Text(Keyboard_App, width=90, height=1)
cipherText.grid(row=1, columnspan=15)

varRow = 2
varColumn = 0

def keypress(event):
    event.char = event.char.lower()
    try:
        buttonL[event.char].configure(highlightbackground='red')
        buttonL[event.char].after(1000, lambda: buttonL[event.char].configure(highlightbackground='#d9d9d9'))
        select(event.char)
        enigmify(event.char)
    except KeyError:
        print('Key outside enigma!')


def select(value):
    if value == '\x08':
        input = plainText.get("1.0", 'end-2c')
        plainText.delete("1.0", END)
        plainText.insert("1.0", input, END)

    elif value == " ":
        plainText.insert(tkinter.END, ' ')
    else:
        plainText.insert(tkinter.END, value)
        
        
def enigmify(value):
    if value == '\x08':
        input = cipherText.get("1.0", 'end-2c')
        cipherText.delete("1.0", END)
        cipherText.insert("1.0", input, END)

    elif value == " ":
        cipherText.insert(tkinter.END, ' ')

    else:
        cipherText.insert(tkinter.END, value)


for button in buttons:
    if button != " Space ":
        but = tkinter.Button(Keyboard_App, text=button, width=5, bg="#000000", fg="#ffffff", highlightthickness=4,
                       activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                       pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x))
        buttonL[button] = but
        but.grid(row=varRow, column=varColumn)

    if button == " Space ":
        but = tkinter.Button(Keyboard_App, text=button, width=60, bg="#000000", fg="#ffffff", highlightthickness=4,
                       activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=4,
                       pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x))
        buttonL[' '] = but
        but.grid(row=6, columnspan=16)
    if button == "<-":
        but = tkinter.Button(Keyboard_App, text=button, width=5, bg="#000000", fg="#ffffff", highlightthickness=4,
                             activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                             pady=4, bd=4, command=lambda x=button, i=varRow - 1, j=varColumn: select(x))
        buttonL['\x08'] = but
        but.grid(row=varRow, column=varColumn)
    varColumn += 1
    if button == '<-' or button == 'l' or button =='m':
        varColumn = 0
        varRow += 1

Keyboard_App.title("La maquina Enigma (version digital)")
Keyboard_App.bind('<Key>', keypress)
Keyboard_App.mainloop()
