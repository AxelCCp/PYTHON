#CLASE PADRE -----------------------------------------------------------------------------------------------------------------------------------------------
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



#CLASE MOTO HEREDA DE VEHICULOS ----------------------------------------------------------------------------------------------------------------------------
class Moto(Vehiculos):
    
    hCaballito = ""

    def caballito(self):
        self.hCaballito = "Voy haciendo el caballito"

    #SE SOBREESCRIBE EL METODO 
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hCaballito)



#CLASE FURGONETA -------------------------------------------------------------------------------------------------------------------------------------------
class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado == True):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


#CLASE Velectricos -----------------------------------------------------------------------------------------------------------------------------------------
class VehiculoElectrico(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargaEnergia(self):
        self.cargando = True

#CLASE BICICLETA ELECTRICA ---------------------------------------------------------------------------------------------------------------------------------
#HERENCIA MULTIPLE, SIEMPRE SE DA REFERENCIA A LA 1RA CLASE Q SE HA COLOCADO EN LOS ARGUMENTOS. SE HEREDAN PRIMERO LOS MÉTODOS DE LA 1RA CLASE HEREDADA. 
class BicicletaElectrica(VehiculoElectrico, Vehiculos):
    pass


#INSTANCIAS
miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici = BicicletaElectrica("marca Ordea", "modelo xxxxx")




