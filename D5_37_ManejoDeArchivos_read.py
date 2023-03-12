
from io import open

#SE LEE EL ARCHIVO EN MODO LECTURA        r
archivo_texto = open("D5_37_archivo.txt","r")

#OBTIENE TODO EL TEXTO EN UN STRING
#texto = archivo_texto.read()
#print(texto)

#OBTIENE EL CONTENIDO DEL ARCHIVO, LINEA A LINEA,  Y LO ALMACENA EN UNA LISTA.
lineas_texto = archivo_texto.readlines()
print(lineas_texto)
print(lineas_texto[0])   #SE ACCEDE A INA LÍNEA EN ESPECIAL

archivo_texto.close()