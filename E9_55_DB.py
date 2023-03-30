#1 SE CREA UN CURSOR PARA CREAR LAS TABLAS DESPUÉS. 
#2 CON EL CURSOR SE EJECUTAN LAS CONSULTAS.  
#3SE COMENTA PARA QUE NO VUELVA A CREAR LA TABLA.

import sqlite3

miConexion = sqlite3.connect("E9_55_PrimeraBase")

miCursor = miConexion.cursor()    #1     

#3                                                   
#miCursor.execute("create table productos(nombre_articulo varchar(50), precio integer, seccion varchar(20))")        #2                       

miCursor.execute("insert into productos values('balon', 15, 'deportes')")

miConexion.commit()

miConexion.close()