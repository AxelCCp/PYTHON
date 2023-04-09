class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de US${}".format(self.nombre, self.cargo, self.salario)
    

listaEmpleados = [
    Empleado("Juan","Director",750000),
    Empleado("Andres","Presidente",600000),
    Empleado("Antonio","Administrativo",450000),
    Empleado("Sara","Secretaria",300000),
    Empleado("Ana","Barrendera",5000),
]


salarios_altos = filter(lambda empleado : empleado.salario > 50000, listaEmpleados)

for empleado_salario  in salarios_altos:
    print(empleado_salario)