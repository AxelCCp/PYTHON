for i in "Python":
    print(i)


print("---------------------")


for i in "Python":
    if i == "h":
        continue
    print(i)


print("---------------------")


nombre = "Píldoras informáticas"
print(len(nombre))

contador = 0;
for i in nombre:
    if i == " ":
        continue
    contador += 1
print(contador)


print("---------------------")


#PASS : APRETA CONTROL + C PARA SALIR DEL BUCLE 
#while True:
    #print("Python")
    #pass
#print("Termino le programa")


print("---------------------")


class MiClase:
    pass #PARA IMPLEMENTAR MÁS TARDE.


print("---------------------")

email = input("Ingresa tu email por favor: ")

for i in email:
    if i == "@":
        arroba = True
        break;
else:
    arroba = False

print(arroba)
