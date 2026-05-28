"""Desarrollar un programa que cargue en tres tuplas los mundiales de fútbol en los cuales Argentina fue campeón,
con el formato (sede, año).
El programa debe calcular y mostrar, para cada mundial, la cantidad de años transcurridos desde la última vez que Argentina había salido campeón."""

a=("Argentina",1978)
b=("Mexico",1986)
c=("Catar",2022)

años1= int(b[1])- int(a[1])
años2= int(c[1])- int(b[1])

print("Cantidad de años desde",a,"a",b," :",años1,"Años",
"\nCantidad de añps desde",b,"a",c," :",años2,"Años")
