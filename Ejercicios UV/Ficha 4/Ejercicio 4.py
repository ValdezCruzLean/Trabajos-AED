"""4. Temperatura diaria
Se solicita realizar un programa que permita ingresar
 tres temperaturas correspondientes a diferentes momentos de un día y determinar:

Cual es el promedio de las temperaturas.
Si existe alguna temperatura que sea mayor al promedio."""

t1 = int(input("ingresar temperatura"))
t2 = int(input("ingresar temperatura"))
t3 = int(input("ingresar temperatura"))

promedio = (t1 + t2 + t3) / 3

if t1 > promedio:
    may = t1
elif t2 > promedio:
    may = t2
elif t3 > promedio:
    may = t3
else:
    may = promedio

print("El promedio de las temperaturas es:", promedio,
      "\n La temperatura mayor es:", may)