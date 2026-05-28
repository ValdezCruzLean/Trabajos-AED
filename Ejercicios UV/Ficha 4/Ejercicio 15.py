"""
15. Dirección de email UTN
Se desea un programa que solicite los datos de un alumno de la UTN:
nombre, apellido y un dominio (con formato regional.utn.edu.ar).

El programa debe:

1. Generar una dirección de correo de la forma:

<primera letra del nombre><apellido>@<dominio> si las iniciales son distintas
<nombre>.<apellido>@<dominio> si las iniciales coinciden
2. Indicar si el alumno pertenece a la provincia de Córdoba o a otra provincia,
considerando que las regionales de Córdoba son:

frc (Córdoba Capital)
frvm (Villa María)
frsf (San Francisco)
"""

nombre = input("Ingrese su nombre :")
apellido = input("Ingrese su apellido :")
dominio = input("Ingrese su dominio en formato 'regional.utn.edu.ar' :")

if nombre[0] == apellido[0]:
	dom = nombre + "." + apellido + "." + dominio
else:
	dom = nombre[0] + "." + apellido + "." + dominio

if dominio[0:3].lower() == "frc":
	provincia = "El alumno pertenece a cordoba capital"
elif dominio[0:4].lower() == "frvm":
	provincia = "El alumno pertenece a villa maria"
elif dominio[0:4].lower() == "frsf":
	provincia = "El alumno pertenece a san francisco"
else:
    provincia = "No es de  arg"
print("El dominio del estudiante es:",dom,"y",provincia)