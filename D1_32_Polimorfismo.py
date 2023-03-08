class Coche():
    def desplazamiento(self):
        print("Me desplazo en 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")


miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

print("-------------------------- POLIMORFISMO --------------------------")

#EL OBJ VEHICULO Q LLEGA POR PARAMETRO, ES EL OBJ QUE SE COMPORTA CON POLIMORFISMO.
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

otroVehiculo1 = Camion()
desplazamientoVehiculo(otroVehiculo1)

otroVehiculo2 = Moto()
desplazamientoVehiculo(otroVehiculo2)

