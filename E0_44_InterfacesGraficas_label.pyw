
from tkinter import *

root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

miImagen = PhotoImage(file="E0_44_Boo.png") #PUEDE SER PNG O GIF

miLabel = Label(miFrame, image=miImagen, text="Hola alumnos de Python!", fg="red", font=("Comic Sans MS",18))
miLabel.place(x=100,y=200)

root.mainloop()
