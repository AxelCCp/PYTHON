
import sqlite3

miConexion = sqlite3.connect("F2_57_GestionProductos")

miCursor = miConexion.cursor()   

#SIN EL AUTOINCREMENT
#miCursor.execute('''
#    create table productos(
#    codigo_articulo varchar(4) primary key,
#    nombre_articulo varchar(50),
#    precio integer,
#    seccion varchar(20)
#    )
#''')

#CON EL AUTOINCREMENT Y UN CAMPO QUE SEA UNICO, QUE NO SE REPITA EL REGISTRO:
miCursor.execute('''
    create table productos(
    id integer primary key autoincrement,
    nombre_articulo varchar(50) unique,
    precio integer,
    seccion varchar(20)
    )
''')

#CON EL AUTOINCREMENT
#miCursor.execute('''
#    create table productos(
#    id integer primary key autoincrement,
#    nombre_articulo varchar(50),
#    precio integer,
#    seccion varchar(20)
#    )
#''')

#SIN EL AUTOINCREMENT
#productos = [
#    ("AR01", "pelota", 20, "jugueteria"),
#    ("AR02", "pantalon", 15, "confeccion"),
#    ("AR03", "destornillador", 25, "ferreteria"),
#    ("AR04", "jarron", 45, "ceramica")
#]

#CON EL AUTOINCREMENT
productos = [
    ("pelota", 20, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("jarron", 45, "ceramica")
]

#SIN EL AUTOINCREMENT
#miCursor.executemany("insert into productos values(?,?,?,?)", productos)

#CON EL AUTOINCREMENT
miCursor.executemany("insert into productos values(NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()