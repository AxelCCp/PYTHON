print("Programa de becas Año 2017")
distanciaEscuela = int(input("Ingresa la distancia a la escuela en KM : "))
print(distanciaEscuela)
numeroHermanos = int(input("Ingresa el número de hermanos en el centro : "))
print(numeroHermanos)
salarioFamiliar = int(input("Introduce salario anual bruto : "))
print(salarioFamiliar)


if(distanciaEscuela>40 and numeroHermanos>2 or salarioFamiliar<=20000):
    print("tienes derecho a beca")
else:
    print("no tienes derecho a beca")