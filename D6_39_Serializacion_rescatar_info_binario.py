#SE RESCATA LA INFO DEL BINARIO QUE SE CREÓ

import pickle

                                        #read binary
ficheroBinario = open("D6_39_listaNombres", "rb")
lista = pickle.load(ficheroBinario)
print(lista)