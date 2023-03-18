#1: AGREGA CAMPO TEXTO.
#2: AGREGA EL SCROLL. CON COMMAND LE DECIMOS Q PERTENECE A TEXTOCOMENTARIO Y CON YVIEW LE DECIMOS Q ES VERTICAL.
#3: nsew : ADAPTA EL  TAMAÑO DEL SCROLL AL CUADRO DE TEXTO.
#4: PARA QUE EL SCROLL NOS INDIQUE EN QUE PARTE DEL CUADRO DE TEXTO ESTAMOS A MEDIDA QUE VAMOS ESCRIBIENDO HACIA ABAJO.
#5: BOTON.
#6: LE DECIMOS Q SE TRATA DE UNA CADENA DE CARACTERES.
#7: SE ASOCIA LA VARIABLE miNombre A CUADRO DE TEXTO cuadroNombre.
#8: CUANDO SE APRETE EL BOTON SE VA A SETTEAR EL NOMBRE CON EL VALOR "JUAN"

from tkinter import *
raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

#----------------------------

miNombre = StringVar()                                      #6

#----------------------------

cuadroNombre = Entry(miFrame, textvariable=miNombre)         #7
cuadroNombre.grid(row=0,column=1, pady=10, padx=10) 
cuadroNombre.config(fg="red", justify="center") 

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1,column=1, pady=10, padx=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2,column=1, pady=10, padx=10)

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=3,column=1, pady=10, padx=10)
cuadroPassword.config(show="*")

textoComentario = Text(miFrame, width=16, height=5)                 #1
textoComentario.grid(row=4,column=1)

scrollVertical = Scrollbar(miFrame, command=textoComentario.yview)  #2
scrollVertical.grid(row=4,column=2,sticky="nsew")     #3
textoComentario.config(yscrollcommand=scrollVertical.set)      #4 

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e", pady=10, padx=10)      

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1,column=0,sticky="e", pady=10, padx=10)   

direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=2,column=0,sticky="e", pady=10, padx=10)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3,column=0,sticky="e", pady=10, padx=10)

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4,column=0,sticky="e", pady=10, padx=10)

def codigoBoton():
    miNombre.set("Juan")            #8

botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)               #5
botonEnvio.pack()

raiz.mainloop()