import math

# 1 - ValueError as ErrorDeNumeroNegativo : se ataja la misma exception que lanza el metodo. con esto el programa puede llegar hasta el "print("Programa terminado")"


def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)


op1=(int(input("Ingresa un número: ")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")