print("""
Conociendo el valor del área (o superficie) de un cuadrado,
 obtenga y muestre el valor del perímetro de ese cuadrado. 
""")

areacuadrado= int(input("Ingrese el Area del cuadrado : "))

#lado = areacuadrado **(1/2)
lado = pow(areacuadrado,0.5)
perimetro = lado * 4

print("EL perimetro del cuadrado Es :",perimetro)