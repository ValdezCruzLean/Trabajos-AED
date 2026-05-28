m1= float(input("Ingrese primer cuerpo"))
m2= float(input("Ingrese segundo cuerpo"))
d= float(input("ingrese distancia entre cuerpos"))
g= 6.673 * pow(10,-8)


resultado= g * ((m1*m2)/d**2)

print("La fuerza de atraccion es:", resultado)