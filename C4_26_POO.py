
# self = this

class Coche():

    #PROPIEDADES
    largochasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    #COMPORTAMIENTO
    def arrancar(self):
        self.enMarcha = True

    #COMPORTAMIENTO
    def estado(self):
        if self.enMarcha == True:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

miCoche = Coche()
print(miCoche.largochasis)
print(miCoche.anchoChasis)

miCoche.arrancar()

print(miCoche.estado())


print("A continuación se crea el siguiente objeto")

miCoche2 = Coche()
print(miCoche2.largochasis)
print(miCoche2.anchoChasis)
print(miCoche2.estado())


