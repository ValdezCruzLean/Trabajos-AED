numero= int(input("Ingrese el numero: "))
cantidad=(0,1,2,3,4,5,6,7,8,9,10)

for i in cantidad:
    multiplicacion = numero * cantidad[i]
    print("5 *", cantidad[i],"=", multiplicacion)