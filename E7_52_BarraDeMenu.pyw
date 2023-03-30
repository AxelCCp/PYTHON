from  tkinter import *
from tkinter import messagebox                #PARA LAS VENTANAS EMERGENTES

root = Tk()


def infoAdicional():
    messagebox.showinfo("Procesador de Juan", "Procesador de textos version 2018")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

#def salirAplicacion():
#    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
#    if(valor == "yes"):
#        root.destroy()

def salirAplicacion():
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")
    print(valor)
    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor == True:
        root.destroy()
        
barraMenu = Menu(root)
root.config(menu = barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)                                                 #tearoff=0 : QUITA UNA LINEA HORIZONTAL Q VIENE POR DEFECTO EN EL DESPLEGABLE.
EdicionMenu = Menu(barraMenu, tearoff=0)
HerramientasMenu = Menu(barraMenu, tearoff=0)
ayudaMenu = Menu(barraMenu, tearoff=0)                                     

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()                                                   #SE AGREGA UN SEPARADOR EN EL DESPLEGABLE
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

barraMenu.add_cascade(label="Edicion", menu=EdicionMenu)
EdicionMenu.add_command(label="Copiar")
EdicionMenu.add_command(label="Cortar")
EdicionMenu.add_command(label="Pegar")

barraMenu.add_cascade(label="Herramientas", menu=HerramientasMenu)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de..", command=infoAdicional)

root.mainloop()
