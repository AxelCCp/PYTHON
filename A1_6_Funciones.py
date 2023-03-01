
#DECLARACIÓN DE LA FUNCIÓN:
#def  : ES PARA DEFINIR LA FUNCIÓN.
def mensaje():
    print("Estamos aprendiendo python");

#LLAMADA A LA FUNCION:
mensaje();


def suma():
    num1 = 5;
    num2 = 10;
    print(num1 + num2);

suma();


def sumaConParametros(num1,num2):
    print(num1 + num2);

sumaConParametros(50, 300);


def restaConParametros(num1,num2):
    return num1 - num2;

print(restaConParametros(30,20));
    

almacenaResultado = restaConParametros(500,45);
print(almacenaResultado);


