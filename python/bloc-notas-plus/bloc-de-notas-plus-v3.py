from tkinter import *
from tkinter import filedialog as f
from io import open

#conf basica

title = " Editor | Bloc de notas+ by FEM Computer"
root = Tk()
root.title(title)

#direccion de archivo
url_file = ""

#funciones del menu

def new_file():
    global url_file
    text.delete(1.0, "end")
    url_file = ""
    root.title(url_file + title)

def open_file():
    global url_file
    url_file = f.askopenfilename(initialdir = '.', filetypes = (("Archivos de texto", "*.txt"),), title = "Abrir archivo")
    if url_file != "":
        file = open(url_file, 'r')
        content = file.read()
        text.delete(1.0, "end")
        text.insert('insert',content)
        file.close()
        root.title(url_file + title)

def save_file():
    global url_file
    if url_file != "":
        content = text.get(1.0,"end-1c")
        file = open(url_file, 'w+')
        file.write(content)
        root.title("Archivo guardado " + url_file + title)
        file.close()
    else:
        file = f.asksaveasfilename(title = "Save file", mode = 'w', defaultextension = ".txt")
        if file is not None:
            url_file = file.name
            content = text.get(1.0,"end-1c")
            file = open(url_file, 'w+')
            file.write(content)
            root.title("Archivo guardado "+ url_file + title)
            file.close()
        else:
            url_file = ""
            root.title("Guardado calcelado "+url_file+title)

#menu

barra = Menu(root)

file_menu = Menu(barra, tearoff = 0)
file_menu.add_command(label = "New file", command=lambda:new_file())
file_menu.add_command(label = "Open file", command=lambda:open_file())
file_menu.add_command(label = "Save file", command=lambda:save_file())
file_menu.add_separator()
file_menu.add_command(label = "Quit", command=lambda:root.quit())
#desplegamos el menu
barra.add_cascade(menu = file_menu, label = "File")

#caja de texto

text = Text(root)
text.pack(fill = "both", expand = 1)
text.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 14))

#ejecucion

root.config(menu = barra)
root.mainloop()
