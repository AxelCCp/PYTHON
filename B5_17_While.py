edad = int(input("Introduce tu edad por favor : "))

while edad<0 or edad>100:
    print("Ha ingresado una edad incorrecta. Vuelva a intentarlo.")
    edad = int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes pasar.")
print("Edad del aspirante: " + str(edad))