
#SE CAMPURAN LAS EXCEPCIONES DE MANERA CONSECUTIVA.

def divide():

    try: 

        op1 = (float(input("ingresa el primer número: ")))
        op2 = (float(input("ingresa el segundo número: ")))
        print("La división es: " + str(op1/op2))

    except ValueError: 

        print("El valor ingresado es erroneo")
    
    except ZeroDivisionError:

        print("No se puede dividir por cero")

    except:

        print("Ha ocurrido un error")

    finally:

        print("Cálculo finalizado")

divide()



print("------------------------------------------------------------------------------------")


def divide2():

    try: 

        op1 = (float(input("ingresa el primer número: ")))
        op2 = (float(input("ingresa el segundo número: ")))
        print("La división es: " + str(op1/op2))

    except ValueError: 

        print("El valor ingresado es erroneo")
    
    except ZeroDivisionError:

        print("No se puede dividir por cero")

    except:

        print("Ha ocurrido un error")

    
    print("Cálculo finalizado")

divide2()


print("------------------------------------------------------------------------------------")


def divide3():

    try: 

        op1 = (float(input("ingresa el primer número: ")))
        op2 = (float(input("ingresa el segundo número: ")))
        print("La división es: " + str(op1/op2))

    
    finally:

        print("Cálculo finalizado")

divide3()

