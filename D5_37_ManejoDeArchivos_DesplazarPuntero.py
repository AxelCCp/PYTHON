#MODIFICA LA POSICIÓN DEL PUNTERO DENTRO DEL TEXTO SANDO PYTHON.
#CON SEEK(), SE DEFINE EL NÚMERO DE CARACTER DONDE QUEREMOS Q SE SITUE EL PUNTERO.

from io import open

archivo_texto = open("D5_37_archivo.txt","r")

#EL ARCHIVO SE LEE, DESPLAZANDOSE EL PUNTERO POR TODO EL ARCHIVO
print(archivo_texto.read())
#LUEGO LE DECIMOS AL PUNTERO QUE VUELVA A LA POSICIÓN 0 Y CON ESTO PUEDE VOLVER A MOSTRAR LA INFO DESDE EL INICIO.
archivo_texto.seek(0)
#REIMPRIME
print(archivo_texto.read())


#TAMBN SE LE PUEDE DECIR A READ() QUE LEA HASTA CIERTO CARACTER
archivo_texto.seek(0)
print(archivo_texto.read(5))


#POSICIONAR EL PUNTERO A LA MITAD DEL TEXTO
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())

#SE SITUA EL PUNTERO AL FINAL DE LA PRIMERA LÍNEA
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())

archivo_texto.close()

