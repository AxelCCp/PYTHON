import re

nombre1 = "Sandra López"
nombre2 = "Antonio Gomez"
nombre3 = "Isabel Gonzalez"

print("................MATCH........................")

if re.match("Sandra", nombre1, re.IGNORECASE):                                              #EL 3ER PARAMETRO ES OPCIONAL PARA IGNORAR MAYUSCULAS Y MINUSCULAS.
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

print("........................................")

nombre4 = "Lara López"
nombre5 = "Jara López"

if re.match(".ara", nombre4, re.IGNORECASE):                                             #CON EL PUNTO SE DICE Q EMPIESE CON CUALQUIER LETRAA, Y A CONTINUACIÓN QUE SIGA CON "ara"
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

print("........................................")

cadena1 = "Jara López"
cadena2 = "3786547385"
cadena3 = "a646464645"

if re.match("\d", cadena3):                                            
    print("Hemos encontrado numero")                                                    #ESTO BUSCA UN NÚMERO AL PRINCIPIO DE LA CADENA
else:
    print("No  hemos encontrado")

print("................SEARCH........................")                                 #BUSCA ALGO EN TODA LA CADENA DE TEXTO.

if re.search("López", nombre1, re.IGNORECASE):                                            
    print("Hemos encontrado el nombre")                                                    
else:
    print("No  hemos encontrado el nombre")

print("........................................")

cod1 = "hgakhgafjhgsdfjskhfds71ksjdhflkshfja"
cod2 = "dhagdja71asd akjhdakhd askdajhdkadk "
cod3 = "jhskdf sldfskjd sdlfkj slkdj dkfj dk"

if re.search("71", cod1):                                            
    print("Hemos encontrado el numero")                                                    
else:
    print("No  hemos encontrado el numero")