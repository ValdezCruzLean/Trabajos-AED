"""9. Edad mínima
Ingresar por teclado las edades de 3 participantes de un concurso.

Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado."""

import random

edad1 = int(input("Ingrese edad del participante"))
edad2 = int(input("Ingrese edad del participante"))
edad3 = int(input("Ingrese edad del participante"))
edadmin = int(input("Ingrese edad minima para participar"))

if edad1 > edadmin and edad2 > edadmin and edad3 > edadmin:
	rta= "TODOS PUEDEN PARTICIPAR"
else:
	rta= "Al menos unos de ellos es un cipallo y se colo"

print(rta)