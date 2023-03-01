import math

print("Programa de calculo de raíz cuadrada")
numero = int(input("Ingresa un número: "))

intentos = 0;

while numero < 0:
    print("No se puede calcular la raíz cuadrada de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado.")
        break;

    numero  = int(input("Ingresa un número: "))

    if numero<0:
        intentos+=1

if intentos<2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es: " + str(solucion))
