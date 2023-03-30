import sqlite3

miConexion = sqlite3.connect("F2_57_GestionProductos")

miCursor = miConexion.cursor()   

miCursor.execute("delete from productos where id = 2")

variosProductos = miCursor.fetchall()    

for producto in variosProductos:
    print(producto)

miConexion.commit()

miConexion.close()