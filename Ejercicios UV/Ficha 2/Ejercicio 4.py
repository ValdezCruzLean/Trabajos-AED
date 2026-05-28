"""
Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado,
 y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado).
Además, para el mismo polinomio, calcule y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.
"""

a = int(input("Ingrese el coeficiente 'a' del polinomio de Segundo Grado : "))
b = int(input("Ingrese el coeficiente 'b' del polinomio de Segundo Grado : "))
c = int(input("Ingrese el coeficiente 'c' del polinomio de Segundo Grado : "))
x = int(input("Ingrese el valor de 'X' del polinomio de Segundo Grado : "))

polinomio = a*(x**2) + b*x + c
discriminante = b**2 - 4*a*c

print("El valor del polinomio con x =",x," es :" , polinomio,
"\nEl valor del discriminante es :",discriminante)