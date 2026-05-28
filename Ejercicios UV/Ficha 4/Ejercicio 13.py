"""
Una empresa nos solicito un programa que nos permita calcular los precios de los productos que vende al publico
para ello, nuestro programa debe pedir el precio unitario, la cantidad que se vendio y si se pago en efectivo o no.
En base a esto determinar

 1) El Precio final sin descuentos del articulo (precio unitario por cantidad)

    2) Calcular un descuento si el usuario pago en efectivo y la cantidad vendida es superior a 10 unidades del 15% caso contrario solo aplicar un 5% de descuento
"""

unidad = int(input("Ingrese el precio unitario"))
cantidad = int(input("Ingrese la cantidad que se venidio"))
pago = input("Eliga metodo de pago EFECTIVO|TARJETA")

preciofinal = unidad * cantidad




if cantidad > 10 and pago.upper() == "EFECTIVO":
	descuento = (preciofinal*15)/100
	precio = preciofinal - descuento
else:
	descuento = (preciofinal*5)/100
	precio = preciofinal - descuento

print("Precio sin descuentos",preciofinal,"$",
"\nArticulo con descuento",precio,"$",
"\nSe aplico un descuento de",descuento,"%")