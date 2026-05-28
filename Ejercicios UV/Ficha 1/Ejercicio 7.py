print("""
Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. 
Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
más un valor extra calculado en base a la cantidad de kilómetros a recorrer:  
Por cada kilómetro a recorrer se cobra $0.30 de adicional.
""")

kilometros= int(input("Ingrese los kilometros hacia su destino : "))
montobase = int(input("Monto Base : "))
extra= kilometros * 0.30
monto= montobase + extra
print("El monto total por el viaje va a ser :", f"{monto:.2f}","$")