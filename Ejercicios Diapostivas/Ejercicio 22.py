import random
numerointento = int(input())
intento = 0
numeroentre = int(input())
numeropc= random.randint(1,numeroentre)
print(numeropc)
while intento < numerointento:
    numeroelegido = int(input())
    if numeroelegido == numeropc:
        print("Ganaste")
        break
    intento += 1

    if intento == numerointento :
        print("PERDISTE")






