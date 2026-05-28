""" 9. Costos del Proyecto
Una pequeña empresa de informática tiene que desarrollar un sistema de información y
para ello tiene un presupuesto de x pesos para cubrir los costos de crear el sistema.
Sabiendo que tiene pensado ganar al menos 17% por el proyecto,
determine cuál es el valor máximo que pueden alcanzar los costos del proyecto."""

presupuesto = float(input(" Ingrese el prespupuesto pare al proyecto : "))
porcentaje = 17

ganancia = (presupuesto * porcentaje) / 100

valormax= presupuesto - ganancia

print("El valor maximo para los costos es :",f"{valormax:.2f}")