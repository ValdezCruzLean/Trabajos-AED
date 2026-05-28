"""Se desea un programa que dados 2 ángulos expresados en grados minutos y segundos,
informe la suma de ambos en grados minutos y segundos."""

a= input("Ingrese angulo : ")
b= input("Ingrese angulo : ")

"""111,59,59"""
seg= int(a[7:9]) + int(b[7:9])
min= int(a[4:6]) + int(b[4:6])
grad= int(a[0:3]) + int(b[0:3])

segcal = divmod(seg,60)


segundos = segcal[1]
mincal = divmod((min + segcal[0]) ,60)
minutos = mincal[1]
grados = grad + mincal[0]


print("Grados::",grados,"Minutos:",minutos,"Segundos:",segundos)
