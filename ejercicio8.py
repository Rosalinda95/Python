#Ejercicio 8. n numeros entre 20 y 60
def numeros():
        n=int(input("Ingresa un numero: "))
        for x in range(n):
                resultado= x+1
        if (resultado>=20 and resultado<=60):
            print(resultado)
numeros()
