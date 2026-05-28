"""10. Tiempos de Triatlon
Un triatlón es una competición deportiva en que los participantes realizan tres carreras:
una de natación, una ciclista y una pedestre.

Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos)
logrados en cada etapa por uno de los deportistas participantes.

Con esos datos determinar:

Tiempo total de la prueba (en formato hh:mm:ss)
Tiempo máximo y mínimo (en segundos)
Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones"""

natacion = input(" Ingrese el timpo en la etapa de natacion ")
ciclista = input(" Ingrese el timpo en la etapa de ciclista ")
pedestre = input(" Ingrese el timpo en la etapa de pedestre ")

segundosnat= int(natacion[0:2]) * 60 + int(natacion[3:5])
segundoscic= int(ciclista[0:2]) * 60 + int(ciclista[3:5])
segundosped =   int(pedestre[0:2]) * 60 + int(pedestre[3:5])

total= segundosnat + segundoscic + segundosped
horas = divmod(total,3600)
hora= horas[0]
minutos = divmod(horas[1],60)
minuto= minutos[0]
segundos = minutos[1]

promedio = (segundosnat + segundoscic + segundosped)/3
tiempomax = max(segundosnat , segundoscic , segundosped)
tiempomin = min(segundosnat , segundoscic , segundosped)


print("Tiempo total de la prueba :",hora,":",minuto,":",segundos,
"\nTiempo Maximo en sgundos :",f"{tiempomax:.2f}",
"\nTiempo Minimo en segundos :",f"{tiempomin:.2f}",
"\nPromedio en segundos",f"{promedio:.2f}")
