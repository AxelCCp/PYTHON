from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    #fichero = filedialog.askopenfilename(title="abrir")
    #fichero = filedialog.askopenfilename(title="abrir", initialdir="C:")                                                                                           #SE PUEDE ESPECIFICAR LA RUTA DONDE DEBE APARECER EL FILE CHOOSER.
    fichero = filedialog.askopenfilename(title="abrir", initialdir="C:", filetypes=(("ficheros de excel", "*.xlsx"), ("ficheros de texto", "*.txt"), ("todos los ficheros", "*.*")))               #INDICA EL TIPO DE FICHERO QUE SE QUIERE ENCONTRAR. SE USA UNA TUPLA. HAY Q PASARLE MINIMO 2 TIPOS DE ARCHIVOS.
    print(fichero)

Button(root, text="abrir fichero", command=abreFichero).pack()

root.mainloop()