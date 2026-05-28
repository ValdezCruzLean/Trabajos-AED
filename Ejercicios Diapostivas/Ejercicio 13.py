"""p1= float(input("Ingrese Calificacion de pacrial 1: "))
p2= float(input("Ingrese Calificacion de pacrial 2: "))
p3= float(input("Ingrese Calificacion de pacrial 3: "))
tp= float(input("Ingrese nota final de trabajos practicos: "))

cpa=0
if p1>= 4:
	cpa +=1
if p2>= 4:
	cpa +=1
if p3>= 4:
	cpa +=1

pp= (p1+p2+p3)/3

condicion= "regular"

if cpa < 3 and tp < 4:
	condicion = "Libre"
elif cpa > 2 and tp >= 4 and pp < 7:
	condicion= "Regular"
elif cpa > 2 and tp >= 8 and pp >= 9:
	condicion= "Aprobado"
elif cpa > 2 and tp >= 8 and pp >= 7:
	condicion = "Promicionado"

print("La condicion del estidiante es", condicion)"""
p1= float(input("Ingrese Calificacion de pacrial 1: "))
p2= float(input("Ingrese Calificacion de pacrial 2: "))
p3= float(input("Ingrese Calificacion de pacrial 3: "))
tp= float(input("Ingrese nota final de trabajos practicos: "))

cpa=0
if p1>= 4:
	cpa +=1
if p2>= 4:
	cpa +=1
if p3>= 4:
	cpa +=1

notas_ok = False

if p1>=7 and p2>= 7 and p3>= 7 and tp >= 8:
	notas_ok = True

pp= (p1+p2+p3)/3

condicion= "regular"

if cpa < 3 or tp < 4:
	condicion = "Libre"
elif notas_ok == True and pp >= 9:
	condicion= "Aprobado"
elif notas_ok == True  and pp >= 7:
	condicion = "Promicionado"

print("La condicion del estidiante es", condicion)
