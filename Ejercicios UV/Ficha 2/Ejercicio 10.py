"""
10. Calculo de Ganancias de Pelicula
Una empresa dedicada al pago de ganancias por las películas que se realizan en los estudios,
necesita un sistema que permita cargar el total que la película recaudó,
el nombre del participante de la película que se tiene que abonar,
el porcentaje que se le debe pagar. Con esos datos mostrar el nombre del actor y el monto que recibirá de las ganancias"""

recaudado= int(input("Ingrese el total que recaudo la pelicula : "))
nombre= input("Ingrese el nombre del participante de la pelicula : ")
porcentaje = float(input("Ingrese el porcentaje de la pelicula que se debe abonar : "))


ganancia = (recaudado * porcentaje)/ 100


print("Nombre del actor :", nombre,
"\nNombre de la pelicula en la que participo : Secretos en la montaña 2",
"\nMonto que recibira por su actuacion :",f"{ganancia:.2f}","$")