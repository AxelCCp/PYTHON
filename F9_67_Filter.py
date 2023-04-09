print(":::::::::::::::FILTER:::::::::::::::::::::::::::::")

def numero_par(num):
    if num % 2 == 0:
        return True

numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numero_par, numeros)))                                #CON EL LIST SE PIDE Q DEVUELVA EL DATO EN FORMATO LISTA, SINO DEVUELVE EL OBJETO.


print(":::::::::::::::FILTER CON LAMBDA::::::::::::::::::")

print(list(filter(lambda numero_par2 : numero_par2 % 2 == 0, numeros))) 