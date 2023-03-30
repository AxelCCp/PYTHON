#1 VARIOS REGISTROS SE AGREGAN CON TUPLAS A LA BBDD.

import sqlite3

miConexion = sqlite3.connect("E9_55_PrimeraBase")

miCursor = miConexion.cursor()      

#1
variosProductos = [
    ("camiseta", 10, "deportes"),
    ("jarron", 90, "ceramica"),
    ("camion", 10, "jugueteria")
]

miCursor.executemany("insert into productos values (?,?,?)", variosProductos)

miConexion.commit()

miConexion.close()