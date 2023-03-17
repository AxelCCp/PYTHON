from tkinter import *

#1: SE CONSTRUYE LA RAIZ. SE LLAMA A LA CLASE TK
#2: ESTO DEJA EL TAMAÑO DE LA VENTANA SIN QUE SE PUEDA REDIMENSIONAR. #(FALSE, FALSE)
#3: PUEDES REDIMENSIONAR SOLO A LO ANCHO. #(TRUE, FALSE)
#4: ICONO
#5: TAMAÑO GUI. SE COMENTA PQ SE USA EN EL "#8" EL FRAME Y LA VENTANA SIEMPRE SE ADAPTA A TAMAÑO DEL FRAME.
#6: COLOR DE FONDO
#7: MAINLOOP() : PARA CREAR LA VENTANA. MAIN LOOP GENERA UN BUCLE INFINITO PARA Q ESTÉ VISIBLE Y A LA ESCUCHA DE LO QUE EL USUARIO HAGA EN LA GUI.
#8: CREAS Y PEGAS EL FRAME A LA VENTANA.
#9: SE PUEDE ANCLAR EL FRAME A LA DERECHA IZQUIERDA ARRIVA ABAJO ... right... left ... bottom .... top
#10: ANCLA EN DOS DIRECCIONES ... "n" = norte ...  "s"= south ... "e" ... "w" ...
#11: SINCRONIZA EL TAMAÑO DE LA VENTANA CON EL DEL FRAME
#12: CONFIGURA BORDE
#13: CAMBIA EL TIPO DE CURSOR

#1
raiz = Tk()
raiz.title("primera ventana")
#2
#raiz.resizable(0,0)
#3
#raiz.resizable(1,0)

raiz.resizable(True,True)
#4
#raiz.iconbitmap("path_archivo/nombrearchivo.ico")
#5
#raiz.geometry("650x350")

#6
raiz.config(background="gray")

#8
miFrame = Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width=650,height=650)

#9
#miFrame.pack(side="bottom")

#10
#miFrame.pack(side="right", anchor="n")

#11
#miFrame.pack(fill="y",expand=True)
#miFrame.pack(fill="x",expand=True)
miFrame.pack(fill="both", expand=True)

#12
#miFrame.config(relief="groove")

#13
#miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")


#7
raiz.mainloop()



