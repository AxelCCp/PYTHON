for i in [1,2,3]:
    print("Hola")

print("")

for i in ["primavera", "verano", "otoño", "invierno"]:
    print("Hola!")

print("")

for i in ["primavera", "verano", "otoño", "invierno"]:
    print(i)

print("")

#CLASE 15
for i in ["Pildoras", "Informáticas", 3]:
    print(i)

print("")

for i in ["Pildoras", "Informáticas", 3]:
    print(i, end=" - ")


print("")


email = False
for i in "juan@pildorasinformaticas.es":
    if(i=="@"):
        email = True
    
if(email == True):
    print("Email correcto")
else:
    print("Email incorrecto")


print("")

email = False
miEmail = input("Ingresa tu email: ")
for i in miEmail:
    if(i=="@"):
        email = True
    
if(email == True):
    print("Email correcto")
else:
    print("Email incorrecto")


print("")


contador = 0
miEmail = input("Ingresa tu email: ")
for i in miEmail:
    if(i=="@") or i==".":
        contador = contador + 1
    
if(contador == 2):
    print("Email correcto")
else:
    print("Email incorrecto")



