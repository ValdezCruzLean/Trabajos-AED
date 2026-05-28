# Desde la pc de lea decimos
#verde = v***e
palabra = input("Ingrese una palabra: ")
primeraLetra = palabra[0]
ultimaLetra = palabra[len(palabra) - 1]
palabraCensurada = "*" * (len(palabra)- 2)
totalPalabra = primeraLetra + palabraCensurada + ultimaLetra
print(totalPalabra)
print(len(palabra))

