print("Verificacion de notas")

notaAlumno = int(input("Introduce tu nota: "))

if(notaAlumno < 5):
    print("insuficiente")

elif(notaAlumno < 6):
    print("suficiente")

elif(notaAlumno < 7):
    print("bien")
    
elif(notaAlumno < 9):
    print("notable")

else:
    print("notable")


print("El programa a finalizado")