def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):                                                #*args : QUIERE DECIR Q PUEDE RECIBIR UN NÚMRO INDETERMINADO DE PARÁMETROS.
        #Acciones adicionales que decoran
        print("Vamos a realizar un calculo:")
        funcion_parametro(*args)

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


suma(7,5)

resta(12,10)

suma2(7,9,8)

