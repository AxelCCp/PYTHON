print("Verificacion de acceso")
edadUsuario = int(input("Introduce tu edad pro favor: "))
if(edadUsuario < 18):
    print("No puedes pasar")

elif(edadUsuario > 120):
    print("Edad incorrecta")
    
else:
    print("Puedes pasar")

print("El programa a finalizado")