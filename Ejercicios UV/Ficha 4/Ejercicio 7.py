"""7. Tirada de moneda
Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente.
Permitir que un jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta."""

import random
apuesta= input("Apueste!!! cara o cruz? ")

moneda=("cara","cruz")

tirada = random.choice(moneda)

if tirada == apuesta.lower():
	rdo= "Ganaste....."
else:
	rdo= "QUE PELOTUDO DE MRDA AJAJAJAJJA PERDISTE AJAJAJAJJA"

print(rdo)