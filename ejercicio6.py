#Ejercicio 6. suma de los cubos de los primeros n números
def cubos():
        a=int(input("Ingrese un numero: "))
        suma=0
        for x in range(a):
                resultado = pow(x+1,3)
        print(x+1,"^3 es:", resultado)
        suma+=resultado

        print("La suma de los cubos es: ", suma)
cubos()
