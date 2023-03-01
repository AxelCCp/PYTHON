#USANDO METODO -----------------
def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num = num + 1
    return miLista

print(generaPares(10))  


#USANDO GENERADOR -----------------
print("")

def generaPares2(limite):
    num = 1
    while num < limite:
        yield num * 2
        num = num + 1
    
devuelvePares = generaPares2(10)

for i in devuelvePares:
    print(i)


#USANDO GENERADOR  y NEXT() -----------------
print("")

def generaPares3(limite):
    num = 1
    while num < limite:
        yield num * 2
        num = num + 1
    
devuelvePares = generaPares3(10)

#DEVUELVE EL 1ER valor DE devuelvePares
print(next(devuelvePares))

print("aquí podría ir más código" 
      + " \n* * * * * * * * * * * *"
      + " \n* * * * * * * * * * * *"
      + " \n* * * P y t h o n * * *"
      + " \n* * * * * * * * * * * *"
      + " \n* * * * * * * * * * * *")

print(next(devuelvePares))

print("aquí podría ir más código" 
      + " \n* * * * * * * * * * * *"
      + " \n* * * * * * * * * * * *"
      + " \n* * * P y t h o n * * *"
      + " \n* * * * * * * * * * * *"
      + " \n* * * * * * * * * * * *")

print(next(devuelvePares))