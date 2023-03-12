from io import open
                                        # r+   : LECTURA Y ESCRITURA
archivo_texto = open("D5_37_archivo.txt","r+")          

archivo_texto.write("Comienzo del texto... ")

#print(archivo_texto.readlines())

#readlines() : ESTO DEVUELVE UNA LISTA 
#AHORA SE GUARDA EN UNA LISTA LO QUE DEVUELVE readlines()
lista_texto = archivo_texto.readlines()
#SE CREA UNA LÍNEA NUEVA
lista_texto[0] = " esta línea ha sido incluida desde el exterior \n"
#POSICIONA EL CURSOR EN 0
archivo_texto.seek(0)
#ESCRIBE LA LÍNEA EN EL TEXTO
archivo_texto.writelines(lista_texto)

#print(archivo_texto.read())

archivo_texto.close()

