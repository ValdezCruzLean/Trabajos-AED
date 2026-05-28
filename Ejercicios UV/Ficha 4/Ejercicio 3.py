'''
Se necesita desarrollar un programa para el área de recursos humanos de una empresa
que permita informar el jornal de un determinado operario.
Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
(1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.

La política de trabajo en la empresa es que los operarios de la misma pueden trabajar
en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es
40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.

'''

codigo = int(input("Ingrese el turno del empleado, 1 si es diurno, 2 si es nocturno"))
hora = int(input("Cantidad de horas trabajadas "))

if codigo == 2:
    salario = hora * 40.60
    turno = "El trabajado es del turno nocturno y cobrará :"
elif codigo == 1:
    salario = hora * 35.50
    turno = "El trabajador es del yurno diurno y cobrará :"
else:
    print("No se reconoce turno")

print(turno, salario)