"""13. Triángulo Rectángulo
Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:

Valor de la hipotenusa (redondeado a 2 decimales)
Valor del lado mayor
Valor del lado menor"""

a= float(input("Ingrese cateto : "))
b= float(input("Ingrese cateto : "))

h= round(pow((a**2 + b**2),(1/2)),2)
mayor= max(a,b)
menor=min(a,b)

print("La hipotenusa es :",h,
"\nEl lado mayor es :", mayor,
"\nEl lado menor es :",menor)