"""11. Galería de arte
Una galería de arte desea preparar un catálogo de sus cuadros más famosos.

Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado.
El programa deberá:

Verificar si todos los cuadros son anteriores al siglo XX
(El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000).
Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
Informar la diferencia en años entre la obra más nueva y la más antigua."""

import random

c1= int(input("Ingrese cnombre de cuadro y año de creacion : "))
c2 = int(input("Ingrese cnombre de cuadro y año de creacion : "))
c3 = int(input("Ingrese cnombre de cuadro y año de creacion : "))
fecha = int(input("ingrese fecha : "))
may = None

men = None


if c1 < 1901 and c2 < 1901  and c3 < 1901:
	rta= "Todas las obras son del siglo XX"
else:
    rta="No todas las obras son del siglo XX"
if c1 == fecha or c2 == fecha or c3 == fecha:
	fechat = "Al menos una de las obras fue creada en la fecha ingresada"
else:
	fechat = "Ninguna de las obras fue creada en la fecha ingresada"

if c1 > c2 and c1 > c3:
	may=c1
elif c2>c3:
	may= c2
else:
	may=c3

if c1 < c2 and c1 < c3:
	men=c1
elif c2 < c3:
	men= c2
else:
	men=c3

diferencia = may-men
print(rta,"\n",fechat,"\nLa diferencia entre el cuadro mas viejo y el mas nuevo es",diferencia)