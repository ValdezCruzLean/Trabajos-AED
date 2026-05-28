"""
9. Datos de un rectángulo
Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el perímetro y la superficie del mismo."""

largo = int(input("Ingrese el largo del rectangulo : "))
ancho= int(input("Ingrese el ancho del rectangulo : "))

area = largo * ancho

perimetro= largo*2 + ancho*2


print("El area del rectangulo es:",area,
"\nEl perimetro del rectangulo es:",perimetro)