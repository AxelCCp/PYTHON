#1 : fetchall() : DEVUELVE UNA LISTA CON TODOS LOS REGISTROS DE LA BASE DE DATOS.
#2 : SE PUEDEN IMPRIMIR LOS REGISTROS ASÍ ...
#3 : ... O BIEN SE PUEDE ITERAR EL RESULTADO. 
#4 : TAMBN SE PUEDE IMPRIMIR ASÍ.

import sqlite3

miConexion = sqlite3.connect("E9_55_PrimeraBase")

miCursor = miConexion.cursor()      

miCursor.execute("select * from productos")

variosProductos = miCursor.fetchall()           #1

#print(variosProductos)     #2

for producto in variosProductos:    #3
    print(producto)

print(".................")

for producto in variosProductos:    #4
    print(producto)

print(".................")

for producto in variosProductos:    #3
    print(producto[0], " -----> ", producto[1], " -----> ", producto[2])