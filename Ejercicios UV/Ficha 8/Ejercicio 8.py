import random

cant = 45_000

random.seed(95)
men = 0
primero = None
segundo = None
pn = True
first4 = True

mult6 = 0
mult9 = 0
mult69 = 0

may4 = 0
for i in range(cant):
    num = random.randint(1, 95_000)
    if i == 0:
        primero = num
    if i == 1 and pn == True:
        segundo = num
        pn = False
    if pn == False:
        if num < segundo:
            men += 1


    if num % 6 == 0:
        mult6 += 1
    if num % 9 == 0:
        mult9 += 1
    if num % 6 == 0 and num % 9 == 0:
        mult69 += 1

    if num % 4 == 0:
        if first4 == True  or  num > may4:
            may4 = num
            first4 = False

if primero < segundo:
    men += 1

porcentaje = (men * 100) / cant

print("Cantidad de números que son menores al segundo numero leído de la secuencia:", men)
print("cantidad de números que son múltiplos de 6:", mult6,
      "\nNumeros múltiplos de 9:", mult9,
      "\nNumeros múltiplos de ambos:", mult69,
      "\nMayor multiplo de 4:", may4,
      "\nPorcentaje de la cantidad de números que son menores al segundo numero leído de la secuencia", porcentaje)