import re

lista_nombres = [
    'Isabel Gomez',
    'María Martín',
    'Sandra López',
    'Sandra Fernández',
    'Santiago Martín'
]

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):                             #  con " ^ " SE ENCUENTRAN LOS ELEMENTOS Q EMPIECEN POR SANDRA.
        print(elemento)

print("::::::::::::::::::::::::::::::::::::::::::::::::")

for elemento in lista_nombres:
    if re.findall('Martín$', elemento):                             #  con $ SE ENCUENTRAN LOS ELEMENTOS Q TERMINEN CON MARTIN
        print(elemento)

print(":::::::::::::::::::::: URLS ::::::::::::::::::::::::::")


lista_urls = [
    'http://pildorasinformaticas.es',
    'http://pildorasinformaticas.com',
    'ftp://pildorasinformaticas.es',
    'ftp://pildorasinformaticas.com'
]

for elemento in lista_urls:
    if re.findall('.es$', elemento):                             
        print(elemento)

print("::::::::::::::::::::::::::::::::::::::::::::::::")

for elemento in lista_urls:
    if re.findall('^ftp', elemento):                             
        print(elemento)


print(":::::::::::::::::::::: URLS 2 ::::::::::::::::::::::::::")

lista_urls2 = [
    'http://pildorasinformaticas.es',
    'http://pildorasinformaticas.com',
    'http://informaticaenespaña.es'
]

for elemento in lista_urls2:
    if re.findall('[ñ]', elemento):                                                             #BUSCA DONDE HAY UNA Ñ                         
        print(elemento)


print(":::::::::::::::::::::: NOMBRES ::::::::::::::::::::::::::")

lista_nombres = [
    'hombres',
    'mujeres',
    'mascotas',
    'niños',
    'niñas',
]

for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento):                                                             #BUSCA NIÑOS O NIÑAS                      
        print(elemento)


print(":::::::::::::::::::::: ELEMENTOS CON O SIN TILDES ::::::::::::::::::::::::::")

lista_tildes= [
    'hombres',
    'mujeres',
    'mascotas',
    'camion',
    'camión',
]

for elemento in lista_tildes:
    if re.findall('cami[oó]n', elemento):                                                                               
        print(elemento)