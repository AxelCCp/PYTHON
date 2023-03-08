
# RAISE : PARA EXCEPTIONS CON MENSAJE PERSONALIZADO.

def evaluaEdad(edad):

    if edad<0:
        raise TypeError("Error... No se permiten edades negativas")

    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "cuidate..."
    
print(evaluaEdad(18))
    