#upper() : PASA A MAYUSCULAS
#LOWER() : PASA A MINUSCULAS
#CAPITALIZE() : PONE LA PRIMERA LETRA EN MAYUSCULA
#COUNT() : CUENTA CUANTAS VECES APARECE UNA LETRA O UNA CADENA DE CARACTERES EN UN STRING.
#FIND() : REPRESENTA LA POSICIÓN DONDE ESTÁ UNA LETRA O CADENA DE CARACTERES.
#ISDIGIT() : DEVUELVE UN BOOLEAN, SI ES UN DIGITO O NO.
#ISALUM() : COMPRUEBA SI HAY SOLO LETRAS. LOS ESPACIOS NO CUENTAN.
#SPLIT() : SEPARA POR PALABRAS USANDO ESPACIOS.
#STRIP() : BORRA ESPACIOS SOBRANTES AL PRINCIPIO Y AL FINAL. 
#REPLACE() : CAMBIA UNA PALABRA O LETRA EN UN STRING POR OTRA.
#RFIND() : REPRESENTA EL NUMERO DE INDICE DE UN CARACTER, PERO ESTE A DIFERENCIA DEL FIND(), CUENTA DESDE ATRAS.

# https://pyspanishdoc.sourceforge.net/lib/string-methods.html

nombreUsuario = input("Ingresa tu nombre de usuario: ")
print("El nombre de usuario es: ", nombreUsuario.upper()) 
print("El nombre de usuario es: ", nombreUsuario.lower()) 
print("El nombre de usuario es: ", nombreUsuario.capitalize()) 


edad = input("ingresa una edad: ")
print(edad.isdigit())


edad2 = input("Ingresa tu edad: ")

while(edad2.isdigit() == False):
    print("Por favor ingresa una valor numérico")
    edad2 = input("Ingresa la edad: ")

if(int(edad2)<18):
    print("No puedes pasar")
else:
    print("Puedes pasar")
 