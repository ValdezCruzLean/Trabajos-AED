"""
Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
(cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos
 tienen un descuento del 35%. Mostrar el precio actual, el monto del descuento y el monto final a pagar."""

precioMedicamento= float(input("Ingrese el precio del medicamento : "))

descuento= (precioMedicamento * 35) / 100


preciofinal = precioMedicamento - descuento

print("El precio del medicamento es :",f"{precioMedicamento:.2f}","$",
"\n Hay un 35% de descuento, vas a ahorrar :",f"{descuento:.2f}","$",
"\n Total a pagar :",f"{preciofinal:.2f}","$")