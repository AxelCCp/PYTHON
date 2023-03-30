import sqlite3

miConexion = sqlite3.connect("F2_57_GestionProductos")

miCursor = miConexion.cursor()   

miCursor.execute("update productos set precio = 35 where nombre_articulo = 'pelota'")

variosProductos = miCursor.fetchall()    

for producto in variosProductos:
    print(producto)

miConexion.commit()

miConexion.close()