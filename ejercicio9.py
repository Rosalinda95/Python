#Ejercicio 9. argumentos de tipo Double para calcular la hipotenusa de un triángulo rectángulo y retorne un valor de tipo Double.
import math
def triangulo():
    a=float(input("ingrese un cateto\n"))
    b=float(input("ingrese el otro cateto\n"))
    c=math.sqrt((a*a+b*b))
    print(str(c))

triangulo()
