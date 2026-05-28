n1= int(input("Ingrese un numero"))
n2= int(input("Ingrese un numero"))
n3= int(input("Ingrese un numero"))
"""Cargar por teclado tres números enteros y determinar y mostrar el mayor de ellos"""
if n1 > n2 and n1 > n3:
	print("Es el mayor:",n1)
else:
	if n2 > n1 and n2 > n3:
		print("Es el mayor:",n2)
	else:
		print("Es el mayor:",n3)