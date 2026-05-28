"""10. Terreno
Se ingresan las medidas de frente y fondo de un terreno.

Determinar si es cuadrado o rectangular y calcular su superficie."""

import random

frente= int(input("Ingrese fondo del terreno : "))
fondo = int(input("Ingrese frente del terreno : "))

area= fondo *frente

if frente == fondo:
	rta= "El terreno es cuadrado y su area es :"
else:
	rta= "El terreno es rectangular y su area es"

print(rta,area)