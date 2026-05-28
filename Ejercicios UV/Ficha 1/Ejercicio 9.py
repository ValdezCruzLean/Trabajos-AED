print("""
Conociendo el valor del perímetro de un rectángulo 
y el valor de uno de los lados de ese rectángulo, calcule 
y muestre el valor del área (o superficie) de ese rectángulo.
""")

perimetro = int(input("Ingrese el perimetro del Rectabgulo : "))
lado = int(input("Ingrese el lado del triangulo : "))

lado2= (perimetro - 2*lado) /2
area= lado * lado2

print("El area del rectangulo es :",area)