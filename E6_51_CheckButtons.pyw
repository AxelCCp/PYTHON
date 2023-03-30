from tkinter import *
root = Tk()
root.title("Ejemplo")

playa = IntVar()
montagna = IntVar()
campo = IntVar()

def opcionesViaje():
    opcionEscogida=""
    if(playa.get() == 1):
        opcionEscogida += " playa"
    if(montagna.get() == 1):
        opcionEscogida += " montaña"
    if(campo.get() == 1):
        opcionEscogida += " campo"

    textoFinal.config(text = opcionEscogida)

foto = PhotoImage(file = "E6_51.png")
Label(root, image = foto).pack()
frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(root, text="playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="campo", variable=campo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()