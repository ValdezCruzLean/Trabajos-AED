k= int(input("kilometros recorridos"))

if k <= 300:
    print("Se debe cobrar 500$ al cliente")
else:
    if k > 300 and k <= 1000:
        excedente= k-300
        total= 500 + excedente*3
        print("Se debe cobrar al cliente:" ,total,"$")
    else:
        excedente= k-300
        total= 500 + excedente * 1.5
        print("Se debe cobrar al cliente:" ,total,"$")