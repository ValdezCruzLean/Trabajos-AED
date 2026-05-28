"""Se conoce el monto del salario actual de un empleado, el nombre del empleado y
 el área funcional al cual pertenece. Se pide calcular el nuevo salario del empleado
sabiendo que obtuvo un incremento del 8% sobre su salario actual y un descuento de 2.5% por servicios,
informando los resultados con el formato que se especifica a continuación:

       Nombre Empleado:  xxxxxxxxx            Nuevo Salario: $ xxx

       Área Funcional:  xxxxxxxxxxxx

       Salario Actual: $ xxxx   """

nombre= input("Ingrese el Nombre del empleado : ")
area= input("Ingrese el area de tranajo del empleado : ")
salario = int(input("Ingrese el monto salarial : "))

incremento = (salario*8)/100
descuento= (salario*2.5)/100

nuevosalario = salario + incremento - descuento

print("Nombre Empleado:\t",nombre,"\t\tNuevo Salario: $", nuevosalario,
      "\nArea Funcional:\t",area,
      "\nSalario Actual: $",salario)