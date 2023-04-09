'''
def area_triangulo(base, altura):
    return (base * altura)/2

print(area_triangulo(5,7))
'''

area_triangulo = lambda base,altura : (base*altura)/2

print(area_triangulo(5,7))
print(area_triangulo(20,9))

triangulo1 = area_triangulo(40,30)
print(triangulo1) 

print("::::::::::::::::::::::::::::::::::")


al_cubo = lambda numero : numero ** 2                           ##TAMBN PUEDE SER ASÍ : al_cubo = lambda numero : pow(numero, 2)

print(al_cubo(13))

print("::::::::::::::::::::::::::::::::::")

destacar_valor = lambda comision : "US$ ¡{}!".format(comision)

comision_daf = 1234567789

print(destacar_valor(comision_daf))