#YIELD FROM : SIMPLiFICA EL CÓDIGO DE LOS GENERADORES EN CASO DE USAR BUCLES ANIDADOS.
#SIRVE PARA ACCEDER A LAS VARIABLES EN MATRICES DE 2 O MÁS DIMENSIONES.
#1.- QUIERE DECIR QUE VA A RRECIBIR UN NÚMERO INDETERMINADO DE ELEMENTOS.


                        #1
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudadesDevueltas))

print(next(ciudadesDevueltas))


print("-------------------------------")

#CON YIELD FROM ...

def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
            yield from elemento

ciudadesDevueltas2 = devuelveCiudades2("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudadesDevueltas2))

print(next(ciudadesDevueltas2))




