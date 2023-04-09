import re 

cadena = "Vamos a aprender expresiones regulares"
print(re.search("aprender", cadena))

print(":::::::::::::::::::::::::::::::::")

textoBuscar = "expresiones"

if re.search(textoBuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

print(":::::::::::::::::::::::::::::::::")


textoBuscar2 = "regulares"
textoEncontrado = re.search(textoBuscar2, cadena)

print(textoEncontrado)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

print("::::::::::::::CADENA 2:::::::::::::::::::")

cadena2 = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar3 = "Python"

print(re.findall(textoBuscar3, cadena2))
print(len(re.findall(textoBuscar3, cadena2)))
