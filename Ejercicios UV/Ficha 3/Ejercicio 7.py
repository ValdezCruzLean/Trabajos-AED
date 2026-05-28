"""En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología.
 El presupuesto anual del hospital se reparte de la siguiente manera:

Área            Presupuesto
Urgencias 	37%
Pediatría 	42%
Traumatología 	21%
 Cargar por teclado el monto del presupuesto total del hospital,
y calcular y mostrar el monto que recibirá cada área. """

presupuesto = int(input("Ingrese el presupuesto total : "))

urgencias = (presupuesto * 37)/100
pediatria = (presupuesto * 42)/100
traumatologia = (presupuesto * 21)/100

print("Presupuesto Total :",presupuesto,
"\nPresupuesto para Area de Urgencias :",urgencias,
"\nPresupuesto para Area de Pediatria :",pediatria,
"\nPresupuesto para Area de Traumatologia :",traumatologia)
