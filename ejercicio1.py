#Ejercicio 1. obtener la media de 3 números.

def Media():
    a=int(input("ingrese el primer numero \n"))
    b=int(input("ingrese el segundo numero \n"))
    c=int(input("ingrese el tercer numero \n"))

    media=((a+b+c)/3)

    print ("la media de los numeros es \n"+ str (media))
Media()
