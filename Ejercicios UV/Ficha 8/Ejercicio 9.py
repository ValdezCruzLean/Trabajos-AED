"""
Desarrolle un programa completo en Python que permita generar una sucesión de 27000 números enteros aleatorios,
 usando como semilla del generador al valor 37 (es decir, random.seed(37)).
Los valores de cada uno de esos 27000 números deben estar entre -20000 y 30000 (incluidos ambos - DEBE usar random.randint(-20000, 30000)
 para generar cada uno de estos números). A partir de esa sucesión, el programa debe:

1 - Determinar cuántos de esos números son mayores o iguales que -20000 pero menores que -5000;
también determinar cuántos números son mayores o iguales a -5000 pero menores que 15000,
y cuántos números son mayores o iguales que 15000 pero además son divisibles por 9.

2 - Determinar el promedio entero de todos los números generados que sean mayores o iguales a
1000 pero que además tengan su último dígito igual a 4 o a 6 (es decir, el resto de dividir por 10 debe ser 4 o 6).
 Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.

3 - Determinar el mayor entre todos los números generados que sean positivos impares, pero que además
tengan su último digito diferente de 1 (es decir, además de ser impar, el resto de dividir por 10 debe ser
diferente de 1).

4 - Determinar el porcentaje entero que la cantidad de números divisibles por 7
representa sobre la cantidad total de números. Observación: en el cálculo de este porcentaje,
 haga primero la multiplicación que corresponda, y luego la división.

"""

import random

random.seed(37)
cant = 27_000

canta= 0
cantb= 0
cantc= 0

cantmod= 0
acumod= 0

may= None
primero = True

cant7 = 0

for i in range (cant):
    num = random.randint(-20000,30000)
    if num >= -20000 and num < -5000:
        canta += 1
    if num >= -5000 and num < 15000:
        cantb += 1

    if num >= 15000 and num % 9 == 0:
        cantc += 1
    if num >= 1000:
        if num % 10 == 4 or num % 10 == 6:
            cantmod += 1
            acumod += num

    if num > 0 and num % 2 != 0 and num % 10 != 1:
        if primero == True or num > may:
            may = num
            primero = False
    if num % 7 == 0 :
        cant7 += 1




promedio = int(acumod/cantmod)

porcentaje =  int((cant7 * 100)/ cant)


print("Cantidad de numeros mayor igual a -20000 pero menores que -5000:",canta,
"\nCantidad de números mayores o iguales a -5000 pero menores que 15000:",cantb,
"\nCantidad de numeros mayores o iguales que 15000 pero además son divisibles por 9:",cantc,
"\nPromedio entero de números mayores o iguales a 1000 que su último dígito igual a 4 o a 6",promedio,
"\nMayor entre todos los números positivos impares que su último digito es diferente de 1:",may,
"\nPorcentaje entero de números divisibles por 7", porcentaje)
