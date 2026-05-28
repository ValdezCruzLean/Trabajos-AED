"""
Leer dos números y calcular:
La suma de sus cuadrados.
El promedio de sus cubos."""

numA = int(input("Ingrese el primer numero : "))
numB = int(input("Ingrese el segundo numero : "))

sumaCuadrados= numA**2 + numB**2
promedioCubos= (numA**3 + numB**3)/2

print("La suma de sus cuadrados es :",sumaCuadrados,
"\n El promedio de sus cubos es :",promedioCubos)