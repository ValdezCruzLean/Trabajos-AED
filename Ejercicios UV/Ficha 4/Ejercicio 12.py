"""Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. A continuación deberá:

   1) Informar si entre las cartas se encuentra el as de espadas

   2) Verificar si las tres cartas son del mismo palo. Si es así, identificar cuál fue la mayor carta.
En caso contrario, informarlo."""

import random

palos = ("Espada", "Basto", "Oro" , "Copa")
numeros = (1,2,3,4,5,6,7,10,11,12)
may = None
c1 = (random.choice(palos), random.choice(numeros))
c2 = (random.choice(palos), random.choice(numeros))
c3 = (random.choice(palos), random.choice(numeros))

if c1[0] == "Espada" and c1[1]==1  or c2[0] == "Espada" and c2[1]==1 or c3[0] == "Espada" and c3[1]==1:
    espada = "Entre las cartas se encuentra el as de espadas"
else:
    espada = "Entre las cartas no se encuentra el as de espadas"
if c1[0] == c2[0] and c2[0] == c3[0]:
    if c1[1] > c2[1] and c1[1] > c3[1]:
        may = c1
    elif c2[1] > c3[1]:
        may = c2
    else:
        may = c3
    rta = "Las cartas son del mismo palo y la mayor es :" + str(may)
else:
    rta = "Las cartas no son del mismo palo"
print(c1,c2,c3)

print(espada, "\n", rta)
