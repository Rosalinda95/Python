#Ejercicio 7. cuadrados de n números mayores a 100.
def cuadrados():
        a=int(input("Ingresa un numero: "))
        for x in range(a):
                resultado = pow(x+1,2)
        if resultado>100:
            print(x+1,"^2 es:", resultado)
cuadrados()
