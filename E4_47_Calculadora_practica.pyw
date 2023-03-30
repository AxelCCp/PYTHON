#1: columnspan: PARA Q USE EL ANCHO DE 4 COLUMNAS. CON ESTO SE ORDENAN LOS BOTONES BAJO LA PANTALLA UNO AL LADO DE OTRO.

from tkinter import *

raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()
operacion = ""
resultado = 0
mathOperator = ""

#PANTALLA ---------------------------------------------------------------------
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=numeroPantalla)                                               #SE ASIGNA numeroPantalla A pantalla.                     
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)  #1
pantalla.config(background="black", fg="orange", justify="right")

#PULSACIONES TECLADO ---------------
def numeroPulsado(num):
    global operacion                                                                                #global : SE LE DICE QUE VA A USAR LA VARIABLE GLOBAL "OPERACION".
    global mathOperator
    mathOperator = operacion
    if(operacion != ""):
        numeroPantalla.set(num)                                                                     #SI OPERACION != "", PONE EN LA PANTALLA EL NUEVO NUMERO INTEGRESADO Y NO CONCATENES CON EL NÚMERO ANTERIOR. 
        operacion = ""                                                                              #SE VUELVE A CADENA VACÍA PARA SE PUEDA SEGUIR CONCATENANDO LOS DIGITOS DEL NUEVO NÚMERO.
    else:
        numeroPantalla.set(numeroPantalla.get() + num)                                              #VEMOS LOS NÚMEROS QUE HAY EN LA PANTALLA Y LUEGO SE CONCATENA CON EL NUEVO NUMERO PULSADO.

#FUNCIÓN SUMA-----------------------
def suma(num):
    global operacion                                                                                #global : SE LE DICE QUE VA A USAR LA VARIABLE GLOBAL "OPERACION".
    global resultado
    resultado += int(num)
    operacion = "suma"
    numeroPantalla.set(resultado)

#FUNCIÓN RESTA----------------------
def resta(num):
    global operacion
    global resultado
    if(resultado != 0):
        resultado -= int(num)
    else:
        resultado = int(num)
    operacion = "resta"
    numeroPantalla.set(resultado)

#FUNCIÓN Mult----------------------
def mult(num):
    global operacion
    global resultado
    if(resultado != 0):
        resultado *= int(num)
    else:
        resultado = int(num)
    
    operacion = "mult"
    numeroPantalla.set(resultado)

#FUNCIÓN Div-----------------------
def div(num):
    global operacion
    global resultado
    if(resultado != 0):
        resultado /= int(num)
    else:
        resultado = int(num)
    operacion = "div"
    numeroPantalla.set(resultado)

#FUNCION EL-RESULTADO---------------
def elResultado():
    global resultado
    global mathOperator
    if(mathOperator == "suma"):
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
    if(mathOperator == "resta"):
        numeroPantalla.set(resultado - int(numeroPantalla.get()))
    if(mathOperator == "mult"):
        numeroPantalla.set(resultado * int(numeroPantalla.get()))
    if(mathOperator == "div"):
        numeroPantalla.set(resultado / int(numeroPantalla.get()))
    resultado = 0

#FILA 1 -----------------------------------------------------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3, command=lambda:div(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)
#FILA 2 -----------------------------------------------------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))                       #lambda : SI NO SE PONE LAMBDA, COMO EL CÓDIGO SE EJECUTA DE ARRIBA HACIA ABAJO, COMMAND LLAMA AUTOMATICAMENTE A numeroPulsado(). Y CON LAMBDA SE CONSIGUE QUE LA FUNCION SOLO SEA LLAMADA SI SE PULSA EL BOTÓN. 
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="X", width=3, command=lambda:mult(numeroPantalla.get()))
botonMult.grid(row=3, column=4)
#FILA 3 -----------------------------------------------------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)
#FILA 4 -----------------------------------------------------------------------
boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda:elResultado())
botonIgual.grid(row=5, column=3)
botonSuma = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)


raiz.mainloop()
