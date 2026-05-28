"""
Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos),
determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel que ha reservado,
¿a qué hora llegara al mismo?"""

partida= input("Ingrese el horario de partida en hh:mm : ")
llegada= input("Ingrese el horario de llegada en hh:mm : ")
hotelminutos = 45

hora = int(llegada[0:2]) - int(partida[0:2])
minutos= int(llegada[3:5])- int(partida[3:5])

duracionViajeAvion = hora*60 +minutos

totalViaje= duracionViajeAvion + hotelminutos

viajeHotelm= int(llegada[3:5]) + hotelminutos

convhor = viajeHotelm // 60
convmin= viajeHotelm % 60

horallegada = int(llegada[0:2]) + convhor


print("El viaje en avion duro:",duracionViajeAvion,"minutos",
"Se llegara al hotel a las" ,str(horallegada)+":"+str(convmin),
"\nLa duracion total del viaje incluyendo el taxi hacia el hotel es:",totalViaje,"minutos")