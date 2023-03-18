#1: SE LE DICE QUE EL CUADRO DE TEXTO, DE TIPO ENTRY, PERTENECE A LA RAIZ.
#2: CREA EL FRAME.
#3: AHORA SE LE DICE AL CUADRO DE TEXTO, Q PERTENECE AL FRAME.
#4: REEMPLAZA PACK POR PLACE, PARA PODER SITUAR EL CUADRO DE TEXTO.
#5: USANDO LABEL DE MANERA NO ACONSEJABLE.

from tkinter import *
raiz = Tk()

#2
miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

#1
#cuadroTexto = Entry(raiz)
#3
cuadroTexto = Entry(miFrame)
#4
#cuadroTexto.pack()
cuadroTexto.place(x=100, y=100)

#5
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.place(x=100,y=100)

raiz.mainloop()