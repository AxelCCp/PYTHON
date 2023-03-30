
import sqlite3

miConexion = sqlite3.connect("F2_57_GestionProductos")

miCursor = miConexion.cursor()   

miCursor.execute("select * from productos")

#miCursor.execute("select * from productos where seccion = 'confeccion'")

variosProductos = miCursor.fetchall()    

for producto in variosProductos:
    print(producto)

miConexion.commit()

miConexion.close()