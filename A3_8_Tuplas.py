#TUPLAS : SON LISTAS INMUTABLES.

#ESTE PROCESO SE LLAMA EMPAQUETADO DE TUPLA:
tupla_1 = ("Juan", 12, 1, 1995);

print(tupla_1[:]);
print(tupla_1[2]);

#PASAR LOS DATOS DE LA TUPLA  --------> A -------> LISTA
lista_1 = list(tupla_1);
print(lista_1);

#PASAR DATOS DE LISTA --------> A -------> TUPLA
tupla_2 = tuple(lista_1);
print(tupla_2);

#BUSCAR UN ELEMENTO EN LA TUPLA
print("Juan" in tupla_2);

#PREGUNTAR CUANTAS VECES SE ENCUENTRA UN ELEEMENTO DENTRO DE UNA TUPLA.... CUANTAS VECES SE ENCUENTRA EL ELEMENTO "12".
print(tupla_2.count(12));

#LONGITUD DE UNA TUPLA
print(len(tupla_2));

#TUPLA UNITARIA ... O SEA CON UN SOLO ELEMENTO ... ESTA DEBE ESTAR ENTRE () Y CON UNA COMA AL FINAL. 
tupla_unitaria_1 = ("Juan",);
print(tupla_unitaria_1[:]);
print(len(tupla_unitaria_1));



#DESEMPAQUETADO DE TUPLA : ESTO ES ASIGNAR LOS VALORES DE UNA TUPLA A DIFERENTES VARIABLES.
tupla_3 = ("Juan", 12, 1, 1995);
nombre, dia, mes, agno = tupla_3;
print("tupla_3 = (Juan, 12, 1, 1995)")
print(nombre);
print(mes);
print(dia);
print(agno);