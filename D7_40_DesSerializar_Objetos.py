import pickle

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


ficheroApertura = open("D7_40_losCoches","rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches: 
    print(c.estado())
    print("")
