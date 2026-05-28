"""8. Lanzamiento de dados
Simular un juego en el que se lanzan dos dados.

Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina."""

import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

suma = dado1 + dado2

if dado1 == dado2 or suma % 2 != 0:
	rdo= "Ganaste....."
else:
	rdo= "QUE PELOTUDO DE MRDA AJAJAJAJJA PERDISTE AJAJAJAJJA"

print(rdo,dado1,dado2,suma)