#Ejercicio 2. obtener el volumen de una esfera

def Volumen():
    a=int(input("ingrese el radio de la esfera \n"))

    volumen = ((4/3)*3.1416)*(a**3)

    print ("el volumen de la esfera es \n"+ str (volumen))

Volumen()
