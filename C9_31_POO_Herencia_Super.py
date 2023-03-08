class Persona():

    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugarResidencia)


class Empleado(Persona):

    #LLAMANDO AL CONSTRUCTOR DE LA CLASE PADRE
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad

    #SOBREESCRIBIENDO METODO DE LA CLASE PADRE
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario, " Antiguedad: ", self.antiguedad)

manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")
manuel.descripcion()

#COMPROBANDO EL TYPE DEL OBJ MANUEL
print(isinstance(manuel, Empleado))
print(isinstance(manuel, Persona))

