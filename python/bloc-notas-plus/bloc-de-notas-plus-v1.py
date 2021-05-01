import tkinter as tk
from tkinter.filedialog import askopenfile
import os

root = tk.Tk()
root.title("Bloc de Notas Plus")
root.geometry("1280x720")

#menu superior

barmenu=tk.Menu(root)

mnuFile=tk.Menu(barmenu)

mnuFile.add_command(label="Open")
mnuFile.add_command(label="New")
mnuFile.add_command(label="Save", command=lambda:saveBtn())
mnuFile.add_command(label="About", command=lambda:aboutBtn())

barmenu.add_cascade(label="File",menu=mnuFile)

root.config(menu=barmenu)

doc="888"

#funciones de los botones del menu

def fileBtn():
    print("hola mundo")


def saveBtn():
    if (doc=="888"):
        saveWin = tk.Tk()
        saveWin.title("Save")
        saveWin.geometry("300x300")
        labelsave = tk.Label(saveWin, text="Type the name of the file")
        labelsave.pack()
        nameBox = tk.Entry(saveWin)
        nameBox.pack()
        saveButton=tk.Button(saveWin, text="Save", command=lambda:saving(), height=1, width=15)
        saveButton.pack()
        def saving():
            doc = nameBox.get()
            file = open(doc, 'w')
            textofile = textBox.get()
            file.write(textofile)
            saveWin.destroy()

    else:
        file = open(doc, 'w')
        textofile = textBox.get()
        file.write(textofile)

def aboutBtn():
    aboutWin = tk.Tk()
    aboutWin.title("About")
    aboutWin.geometry("300x300")

    aboutWin.mainloop()

#Cuadro de texto

textBox = tk.Text()
textBox.pack()
#textBox.place(x = 10, y = 10, width=1260, height=700)

root.mainloop()
