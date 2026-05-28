"""
Conociendo el precio de lista de un artículo, determinar:

Precio de venta al contado (10% de descuento)
Precio de venta con tarjeta (5% de recargo)"""

precioLista= int(input("Ingrese el precio de la lista : "))

descuento = (precioLista * 10)/100
recargo= (precioLista * 5)/100

preciocontado = precioLista - descuento
preciotarjeta= precioLista + recargo

print("Precio de venta al contado:",f"{preciocontado:.2f}","$",", ahorras:",f"{descuento:.2f}","$",
"\nPrecio de venta con tarjeta:",f"{preciotarjeta:.2f}","$",", se agrego un racargo de:",f"{recargo:.2f}","$")