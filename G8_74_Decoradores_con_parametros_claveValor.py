def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):                                                
        #Acciones adicionales que decoran
        print("Vamos a realizar un calculo:")
        funcion_parametro(*args, **kwargs)

        #Acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcion_interior


@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def suma2(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

@funcion_decoradora
def potencia2(base, exponente):
    print(pow(base, exponente))

print("....................")
suma(7,5)
print("....................")
resta(12,10)
print("....................")
suma2(7,9,8)
print("....................")
potencia(5,3)
print("....................")
potencia2(base = 5, exponente = 3)                          #AQUÍ ES UTIL **kwargs ... CUANDO SE USA NOMBRE = VALOR.

