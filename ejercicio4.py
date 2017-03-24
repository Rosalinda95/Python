a=int (input ("ingrese el primer numero"))
b=int (input ("ingrese el segundo numero"))
c=int (input ("ingrese el tercer numero"))

if (a > b and a > c):
	print("El numero mayor es " + str(a))
else:
	if (b > a and b > c):
		print("El numero mayor es " + str(b))
	else:
		print("El numero mayor es " + str(c))
