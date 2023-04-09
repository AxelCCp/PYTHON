class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de US${}".format(self.nombre, self.cargo, self.salario)
    

listaEmpleados = [
    Empleado("Juan","Director",7500),
    Empleado("Andres","Presidente",6000),
    Empleado("Antonio","Administrativo",4500),
    Empleado("Sara","Secretaria",3000),
    Empleado("Ana","Barrendera",300),
]


def calculo_comision(empleado):
    if(empleado.salario < 3200 and empleado.nombre != "Ana"):
        empleado.salario = empleado.salario * 1.03
    return empleado

listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)

