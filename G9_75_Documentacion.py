def areaCuadrado(lado):
    """Calcula el area de un cuadrado."""
    return "El area del cuadrado es: " + str(lado * lado)

def areaTriangulo(base, altura):
    """Calcula el area de un triangulo."""
    return "El area del triangulo es: " + str((base * altura) / 2)

print(areaCuadrado(3))
print(areaCuadrado.__doc__)                                                                         #LE DECIMOS Q IMPRIMA LA DOCUMENTACION ASOCIADA AL METODO.

print("............................")
 
print(areaTriangulo(20,15))
help(areaTriangulo)