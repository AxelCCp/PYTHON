salarioPresidente = int(input("Introduce salario presidente: "))
print("Salario Presidente : " + str(salarioPresidente));

salarioDirector = int(input("Introduce salario director: "))
print("Salario director : " + str(salarioDirector));

salarioJefeArea = int(input("Introduce salario jefe de area: "))
print("Salario jefe de area : " + str(salarioJefeArea));

salarioAdministrativo = int(input("Introduce salario administrativo: "))
print("Salario administrativo : " + str(salarioAdministrativo));

if(salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente):
    print("Todo funciona OK")
else: 
    print("algo falla en la empresa")