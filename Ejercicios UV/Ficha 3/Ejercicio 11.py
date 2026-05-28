"""Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada,
mostrando la primer letra y la última, pero reemplazando los caracteres intermedios por asteriscos.

Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”."""

palabra=input("Ingrese una palabra : ")

asteriscos = len(palabra) -2

nuevapalabra = palabra[0]+ "*" * asteriscos + palabra[-1]

print("Palabra enmascarada :",nuevapalabra)