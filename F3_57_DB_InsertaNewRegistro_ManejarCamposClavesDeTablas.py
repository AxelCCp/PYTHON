
import sqlite3

miConexion = sqlite3.connect("F2_57_GestionProductos")

miCursor = miConexion.cursor()   

#SIN EL AUTOINCREMENT
#miCursor.execute("insert into productos values ('AR05', 'tren', 15, 'jugueteria')")

#CON EL AUTOINCREMENT
miCursor.execute("insert into productos values (NULL,'tren', 15, 'jugueteria')")

miConexion.commit()

miConexion.close()