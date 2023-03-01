def evaluacion(nota):
    valoracion = "aprobado"
    if nota<5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(7))


#INGRESAR DATOS POR TECLADO
print("Programa de evaluación de notas de alumno")

#notaAlumno = input();   //TAMBN PUDE IR SIN EL PARAMETRO STRING.
notaAlumno = input("ingresa la nota del alumno:");

#INT() : ES PARA PASAR DE STRING A INT, YA QUE AL RECIBIR EL VALOR DESDE EL INPUT, LO CONSIDERA COMO STRING.
print(evaluacion(int(notaAlumno)))


