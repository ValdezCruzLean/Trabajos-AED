'''num= int(input("ingrese un numero"))
may= num

while num != 0:
	num= int(input("ingrese un numero"))
	if num > may:
		may = num

print(may)'''

cantidadIteraciones = int(input("ingrese la cantidad de numeros que quiere introducir"))
numero= int(input("ingrese un numero"))
for i in range(cantidadIteraciones):
	numero= int(input("ingrese un numero"))
	if i==0 or cantidadIteraciones> may:
	    may= numero

print(may)