
# self = this

class Coche():

    #CONSTRUCTOR
    def __init__(self):
        self.__largochasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4                               # "__" : ESTO ES UN PRIVATE
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha == True: 
            chequeo = self.__chequeo_interno()

        if self.__enMarcha == True and chequeo == True:
            return "El coche está en marcha"
        elif(self.__enMarcha == True and chequeo == False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar."
        else:
            return "El coche está parado"

    def estado(self):
        print("el coche tiene ",  self.__ruedas, "ruedas. un ancho de ",  self.__anchoChasis,  " y un largo de ", + self.__largochasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


#COCHE 1
miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("\n----------------------------- A continuación se crea el siguiente objeto --------------------------------\n")

#COCHE 2
miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()


