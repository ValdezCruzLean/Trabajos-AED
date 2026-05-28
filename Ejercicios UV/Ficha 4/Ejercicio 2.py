"""
2. Suma - División - Potencia
Se necesita desarrollar un programa que permita calcular la suma de tres números.
Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
en caso contrario elevar el resultado al cubo.
"""

a = int(input("Ingrese un numero : "))
b = int(input("Ingrese un numero : "))
c = int(input("Ingrese un numero : "))

suma = a + b + c

if suma > 10:
	calculo= int(suma/2)
	rta= "La suma es " + str(suma) + " el resultado se dividio en 2 :"
else:
	calculo= suma **3
	rta= "La suma es " + str(suma) + " el resultado se elevo al cubo :"
print(rta,calculo)