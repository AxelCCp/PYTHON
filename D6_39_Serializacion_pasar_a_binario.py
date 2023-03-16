#SERIALIZACIÓN : GUARDAR UN OBJ EN UNA COLECCION DE BYTES
#SE IMPORTA LA BIBLIOTECA PICKE QUE TIENE LOS MÉTODOS PARA SERIALIZAR
import pickle

D6_39_listaNombres = ["Pedro","Maria","Isabel","Vale"]
                                  #WB : SE LE DICE WRITE BYTES
ficheroBinario = open("D6_39_listaNombres", "wb")

#SE HACE UN VOLCADO DE LA LISTA AL FICHERO EXTERNO
pickle.dump(D6_39_listaNombres, ficheroBinario)

ficheroBinario.close()

del(ficheroBinario)