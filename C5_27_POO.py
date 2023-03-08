
# self = this

class Coche():

    #PROPIEDADES
    largochasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    #COMPORTAMIENTO
    def arrancar(self, arrancamos):

        self.enMarcha = arrancamos

        if self.enMarcha == True:
            return "El coche está en marcha"
        else:
            return "El coche está parado"


    #COMPORTAMIENTO
    def estado(self):
        print("el coche tiene ",  self.ruedas, "ruedas. un ancho de ",  self.anchoChasis,  " y un largo de ", + self.largochasis)

miCoche = Coche()
print(miCoche.largochasis)
print(miCoche.anchoChasis)
print(miCoche.arrancar(True))
miCoche.estado()


print("\n----------------------------- A continuación se crea el siguiente objeto --------------------------------\n")

miCoche2 = Coche()
print(miCoche2.largochasis)
print(miCoche2.anchoChasis)
print(miCoche2.arrancar(False))
miCoche2.estado()


