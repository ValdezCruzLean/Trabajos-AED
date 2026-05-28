"""6. Analisis de palabra
Se pide un programa que le solicite al usuario que ingrese una palabra.
Con esa palabra calcular los siguientes puntos:

Determinar la cantidad de letras que tiene  la palabra.
Mostrar un mensaje que informe si la palabra termina en vocal."""

palabra = input("Ingrese una palabra : ")

num = len(palabra)
letrafinal= palabra[-1].lower()

if letrafinal == "a" or letrafinal == "e" or letrafinal  == "i" or letrafinal  == "o" or letrafinal == "u":

    rta= "La palabra termina en vocal"
else:
    rta= "La palabra no termina en vocal"

print("La la pabra ctiene una cantidad de",num,"letras",
"\n ;D",rta)