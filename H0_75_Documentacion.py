from D3_34_MODULOS import A0_34_Modulos_FuncionesMatematicas

class Areas:

    """Clase que calcula el area de figuras geométricas."""

    def areaCuadrado(lado):
        """Calcula el area de un cuadrado."""
        return "El area del cuadrado es: " + str(lado * lado)

    def areaTriangulo(base, altura):
        """Calcula el area de un triangulo."""
        return "El area del triangulo es: " + str((base * altura) / 2)


help(Areas)

print("............................")

print(Areas.areaCuadrado(3))                                                                       

print("............................")
    
print(Areas.areaTriangulo(20,15))
help(Areas.areaTriangulo)

print("............DOCUMENTACION DE MODULOS................")

help(A0_34_Modulos_FuncionesMatematicas)