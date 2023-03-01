print("Asignaturas 2017")
print("Informática grafica - Pruebas de Software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")

#SE PASA TODO A MINUSCULAS
asignatura = opcion.lower()

# VA A COMPARAR EL VALOR QUE HAY EN ASIGNATURA CON LOS VALORES DADOS CON IN
if asignatura in ("informática grafica, pruebas de software, usabilidad y accesibilidad"):
    print("Asignatura escogida: " + asignatura)

else:
    print("La asignatura escogida no está contemplada") 

