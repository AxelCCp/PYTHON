#open : METODO PARA ABRIR UN ARCHIVO EXTERNO. PIDE 2 ARGUMENTOS. EL NOMBRE DEL ARCHIVO QUE SE VA A ABRIR Y EL MODO EN QUE SE VA A ABRIR. 
#EL ARCHIVO SE PUEDE ABRIR EN MODO LECTURA, ESCRITURA, APPEND PARA AGREGAR INFO A UN ARCHI QUE YA EXISTE. 

from io import open

#CON ESTO CREA EL ARCHIVO
archivo_texto = open("D5_37_archivo.txt","w")

frase = "Buen día para aprender python ..."
archivo_texto.write(frase)
archivo_texto.close()

