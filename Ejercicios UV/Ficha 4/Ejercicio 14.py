"""
La empresa de peajes AED Pase-Pase S.R.L, festeja su séptimo aniversario y,
por tal motivo, el día de hoy ofrece premios a a sus clientes.

Estos premios se calculan de la siguiente manera:

1) Cada vez que pasa un cliente, se sortea un número del 0 al 9.
Si el número coincide con el último dígito de la patente del vehículo,
se le cobra la tarifa promocional de $50, si no, se le cobra la tarifa estándar de $90

2) Independientemente de la tarifa que deba pagar,
si el último dígito de la patente es 7,
entonces recibe un descuento del 50%, en caso contrario un descuento del 10%.

Desarrolle un programa en Python que le solicite al usuario los dígitos de su patente (únicamente los dígitos),
 simule su paso por el peaje e indique el monto a abonar.
"""

import random

num = random.randint(0,9)
patente = input("Ingrese su patente")
ultd = int(patente[-1])
tarifa = None
if ultd == num:
	tarifa = 50
else:
	tarifa = 90
if ultd == 7:
	descuento = (tarifa * 50)/100
else:
	descuento = (tarifa * 10)/100

tarifafinal = tarifa - descuento

print("El numero sorteado es",num,"y el ultimo digito de la patente es",ultd,
"\nLa tarifa sera igual a",tarifa,"$",
"\nEl la tarifa final que debera pagar es",tarifafinal)