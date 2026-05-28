"""Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100,
que representaria la tarjeta de bingo de una persona. Una vez generados
los números aleatorios solicitar al usuario que ingrese 3 números enteros y
a partir de alli mostrar los siguientes mensajes:

Si el usuario no marcó ninguno de los números indicarlo diciendo
"El jugador tiene mala suerte, no marcó ninguna casilla"
Caso contrario mostrar "El jugador marcó algún numero de la tarjeta"."""

import random
billete =(random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100),
random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),
random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
print(billete)

numero1 = int(input("ingrese numero "))
numero2 = int(input("ingrese numero "))
numero3 = int(input("ingrese numero "))

if numero1 in billete or numero2 in billete or numero3 in billete:
    resultado ="El jugador marcó algún numero de la tarjeta"
else:
    resultado = "El jugador tiene mala suerte, no marcó ninguna casilla"

print(resultado)