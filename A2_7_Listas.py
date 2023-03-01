miLista = ["maria", "pepe", "marta", "antonio"];

#CON [:] SE IMPRIME LA LISTA COMPLETA.
print(miLista[:]);    

#DESDE 0 HASTA N
print(miLista[1]);

#PARTE DESDE -1 HASTA N, DESDE EL ULTIMO ELEMENTO DE LA LISTA
print(miLista[-1]);

#IMPRIME DEL 0 AL 1
print(miLista[0:2]);

#IMPRIME EL INDICE 1
print(miLista[1:2]);

#IMPRIME LOS DOS ULT ELEMENTOS
print(miLista[2:]);

#AGREGAR ELEEMENTOS A LA LISTA
miLista.append("Sandra");
print(miLista[:]);  

#AGREGAR ELEMENTOS EN UNA POSICIÓN ESPECIFICA
miLista.insert(2,"Elefante");
print(miLista[:]);  

#AGREGAR MÁS ELEMENTOS, USANDO UNA LISTA
miLista.extend(["Tigre","León","Tortuga"]);
print(miLista[:]);  

#PARA SABER EL INDICE DE UN ELEMENTO
indice = miLista.index("Tigre");
print(indice);

#SI SE BUSCA EL INDICE DE UN ELEMENTO Y HAY 2 ELENTOS CON EL MISMO NOMBRE, TE DA EL PRIMERO
miLista.extend(["Tortuga", "Vaca"]);
print(miLista[:]); 
indice2 = miLista.index("Tortuga");
print(indice2);

#IMPRIME TRUE OR FALSE, SI UN ELEMENTO ESTÁ EN LA LISTA
print("pepe" in miLista);

#LAS LISTAS PUEDEN ALMACENAR DIFERENTES TIPOS DE DATOS
miLista_2 = [True, 10, "Sandra", 30.34]; 
print(miLista_2);

#ELIMINAR ELEMENTOS DE LA LISTA
miLista.remove("maria")
print(miLista[:]);

#ELIMINA EL ÚLTIMO ELEMENTO DE LA LISTA
miLista.pop();
print(miLista[:]);

#SUMAR 2 LISTAS 
nuevalista_1 = ["Sandra", 3, 3.56, True];
nuevalista_2 = [45, 78.32, False, "Pepe"];
nuevalista_3 = nuevalista_1 + nuevalista_2;
print(nuevalista_3[:]);

#MULTIPLICA UNA LISTA
nuevalista_4 = ["Angela", 35, 170.50, True] * 7;
print(nuevalista_4);
