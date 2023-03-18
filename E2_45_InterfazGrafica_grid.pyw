#1: EL GRID GENERA UNA TABLA Y RECIBE LOS INDICES DE FILA Y COLUMNA.
#2: SE USA STICKY QUE USA LOS PUNTOS CARDINALES PARA LA ALINEACIÓN DE TEXTO.
#3: SE APLICA PADING X e Y ... ESPACIADO.
#4: SE PUEDE CAMBIAR EL COLOR DEL TEXTO.
#5: NAMEJA LA ALINEACIÓN DEL TEXTO center ... right ... left 
#6: PASSWORD.

from tkinter import *
raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0,column=1, pady=10, padx=10) #1
cuadroNombre.config(fg="red", justify="center") #4  #5

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1,column=1, pady=10, padx=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2,column=1, pady=10, padx=10)

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=3,column=1, pady=10, padx=10)
cuadroPassword.config(show="*")

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e", pady=10, padx=10)      #2

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1,column=0,sticky="e", pady=10, padx=10)   #3

direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=2,column=0,sticky="e", pady=10, padx=10)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3,column=0,sticky="e", pady=10, padx=10)

raiz.mainloop()