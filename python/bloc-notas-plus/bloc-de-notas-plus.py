import tkinter as tk
from tkinter.filedialog import askopenfile
import os

root = tk.Tk()
root.title("Bloc de Notas Plus")
root.geometry("1280x720")

#menu superior
def fileBtn():
    print("hola mundo")

fileText = tk.StringVar()
fileButton = tk.Button(root, textvariable=fileText, command=lambda:fileBtn(), height=1, width=15)
fileText.set("File")
fileButton.grid(column=1, row=1)

def saveBtn():
    file = open('file.txt', 'w')
    textofile = textBox.get()
    file.write(textofile)

saveText = tk.StringVar()
saveButton = tk.Button(root, textvariable=saveText, command=lambda:saveBtn(), height=1, width=15)
saveText.set("Save")
saveButton.grid(column=2, row=1)

def aboutBtn():
    aboutWin = tk.Tk()
    aboutWin.title("About")
    aboutWin.geometry("300x300")

    aboutWin.mainloop()

aboutText = tk.StringVar()
aboutButton = tk.Button(root, textvariable=aboutText, command=lambda:aboutBtn(), height=1, width=15)
aboutText.set("About")
aboutButton.grid(column=3, row=1)

#Cuadro de texto

textBox = tk.Entry(root)
textBox.grid(column=2, row=2)

root.mainloop()