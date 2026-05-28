"""15. Fecha patria
Desarrollar un programa en Python que, a partir de una fecha patria almacenada en una tupla (día, mes, año)
genere otras dos tuplas con las fechas correspondientes al centenario y bicentenario.
Mostrar en pantalla las tres fechas."""


fecha=(10,"Mayo",1810)

centenario=(fecha[0],fecha[1], (int(fecha[2]))+100)
bicentenario=(fecha[0],fecha[1], (int(fecha[2]))+200)

print(fecha,"\n",centenario,"\n",bicentenario)