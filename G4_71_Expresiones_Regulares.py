import re

lista_nombres = [
    'ana',
    'pedro',
    'maría',
    'rosa',
    'sandra',
    'celia',
]

                                                            #ENCUENTRA PALABRAS SEGÚN UN RANGO DE CARACTERES

for elemento in lista_nombres:
    if re.findall('[o-t]', elemento):                                                                               
        print(elemento)

print("::::::::::::::::::::::::::::::::::::::::::::::::")


for elemento in lista_nombres:                          #ENCUENTRA PALABRAS QUE EMPIEZAN CON UN RANGO DE CARACTERES
    if re.findall('^[o-t]', elemento):                  #ESTO DISTINGUE MINUSCULAS DE MAYUSCULAS, ASI Q SI EMPIEZAN CON MAYUSCULAS '^[O-T]'                                                                    
        print(elemento)

print("::::::::::::::::::::::::::::::::::::::::::::::::")

for elemento in lista_nombres:                          #ENCUENTRA PALABRAS QUE TERMINAN CON UN RANGO DE CARACTERES
    if re.findall('[o-t]$', elemento):                                                                                     
        print(elemento)


print("::::::::::::::::::::LISTA DE CODIGOS 1::::::::::::::::::::::::::::")

lista_codigos = [
    'Ma1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma3',
    'Va1',
    'Va2',
    'Ma4'
]

for elemento in lista_codigos:                          
    if re.findall('Ma[0-3]', elemento):                                         # SE OBTIENEN LOS ELEMENTOS Ma DEL 0 AL 3                                                                         
        print(elemento)

print("::::::::::::::::::::::::::::::::::::::::::::::::")

for elemento in lista_codigos:                          
    if re.findall('Ma[^0-3]', elemento):                                        # SE OBTIENEN LOS ELEMENTOS OPUESTOS A Ma DEL 0 AL 3                                                                                    
        print(elemento)

print("::::::::::::::::::::LISTA DE CODIGOS 2::::::::::::::::::::::::::::")

lista_codigos2 = [
    'Ma1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma3',
    'Va1',
    'Va2',
    'Ma4',
    'MaA',
    'Ma5',
    'MaB',
    'MaC'
]

for elemento in lista_codigos2:                          
    if re.findall('Ma[0-3A-B]', elemento):                                                                                                                         
        print(elemento)

print("::::::::::::::::::::LISTA DE CODIGOS 3::::::::::::::::::::::::::::")


lista_codigos3 = [
    'Ma.1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma:3',
    'Va1',
    'Va2',
    'Ma4',
    'MaA',
    'Ma.5',
    'MaB',
    'Ma:C'
]

for elemento in lista_codigos3:                          
    if re.findall('Ma[.:]', elemento):                                                  #DEVUELVE LOS ELEMENTOS CON UNO A DOS PUNTOS                                                                                                                       
        print(elemento)