for i in range(5):
    print(f"El valor de la variable i es :  {i}")

print("")

#del 20 al 25
for i in range(20,24):
    print(f"El valor de la variable i es :  {i}")

print("")


#del 40 al 79 de 3 en 3
for i in range(40,80,3):
    print(f"El valor de la variable i es :  {i}")

print("")

#-----

valido = False
email = input("Ingresa un email: ")
for i in range(len(email)):
    if(email[i] == "@"):
        valido = True

if(valido == True):
    print("Email correct")
else:
    print("Email incorrecto")
