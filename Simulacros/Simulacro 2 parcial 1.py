import random
sucecion = 25_000

mult3 =0
mult5n3=0
num11a= 0
num11c= 0
numn = 0
primerdig = None
primero = True
may = None
random.seed(20220512)
for i in range(sucecion):
    num = random.randint(1, 45_000)
    numstr = str(num)
    primerdig = int(numstr[0])

    if primero == True or primerdig == 1 and num > may:
        may = num
        primero = False

    if num %3 == 0:
        mult3 +=1
    elif num % 5 == 0:
        mult5n3 +=1
    else:
        numn +=1

    if num % 2 == 0 and num % 11 == 0:
        num11c +=1
        num11a += num

promedio = int(num11a/num11c)
porcentaje3 = int((mult3*100)/sucecion)
porcentaje5n3 = int((mult5n3*100)/sucecion)
porcentajen = int((numn*100)/sucecion)


print("Cantidad de numeros multiplos de 3:", mult3,
"\nCantidad de numeros multiplo de 5 y no de 3:", mult5n3,
"\nCantidad de numeros que no son multiplo de 3 o 5:", numn,
"\nNumero mayor que empieza con numero 1:", may,
"\nPromedio de numeros  pares y multiplo de 11:",promedio,
"\nPorcentaje de multiplos de 3:",porcentaje3,
"\nPorcentaje de multiplos de 5 y no de 3 :", porcentaje5n3,
"\nPorcentaje numeros que no son multiplos de 3 o 5:",porcentajen
      )