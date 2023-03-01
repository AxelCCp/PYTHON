
#DICCIONARIOS
#TIENEN ESTRUCTURA DE CLAVE Y VALOR.

diccionario_1 = {"Alemania" : "Berlín", "Francia" : "París", "UK" : "Londres", "España" : "Madrid"}
print(diccionario_1)
print(diccionario_1["Francia"])


#AGREGAR ELEMENTO AL DICCIONARIO
    #SE AGREGA A PROPOSITO UN ELEMENTO ERRONEO

diccionario_1["Italia"] = "Lisboa"
print(diccionario_1)

#AHORA SE MODIFICA EL ELEMENTO ERRONEO DEL DICCIONARIO.

diccionario_1["Italia"] = "Roma"
print(diccionario_1)

#ELIMINAR ELEMENTO

del diccionario_1["UK"]
print(diccionario_1)

#-------- DICCIONARIO CON DIFERENTES TIPOS
diccionario_2 = {"Alemania" : "Berlín", 23 : "Jordan", "Mosqueteros" : 3}
print(diccionario_2)


#-------- ASIGNAR LOS ELEMENTOS DE UNA TUPLA, COMO LAS CLAVES DE UN DICCIONARIO
tupla_1 = ("España", "Francia", "UK", "Alemania")
diccionario_3 = {tupla_1[0] : "Madrid", tupla_1[1] : "París", tupla_1[2] : "Londres", tupla_1[3] : "Berlín"}
print(diccionario_3)
print(diccionario_3["Francia"])


#HACER QUE UN DICCIONARIO ALMACENE UNA TUPLA ENTERA DE VALORES
diccionario_4 = {23 : "Jordan", "Nombre" : "Michael", "Equipo" : "Chicago", "Anillos" : (1991, 1992, 1993, 1996, 1997, 1998)}
print(diccionario_4)
print(diccionario_4["Equipo"])
print(diccionario_4["Anillos"])


#ASIGNAR UN DICCIONARIO DENTRO DE OTRO DICCIONARIO
diccionario_5 = {23 : "Jordan", "Nombre" : "Michael", "Equipo" : "Chicago", "Anillos" : {"temporadas" : (1991, 1992, 1993, 1996, 1997, 1998)}}
print(diccionario_5)
print(diccionario_5["Anillos"])

print(diccionario_5.keys())
print(diccionario_5.values())

print(len(diccionario_5))


