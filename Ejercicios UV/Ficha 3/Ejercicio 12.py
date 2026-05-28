"""En la disciplina olímpica una de las pruebas mas esperadas en la natacion es la posta 4x100.
En esta disciplina el equipo ganador registró los siguientes tiempos en cada estilo:

Espalda: 52 segundos 15 centésimas.
Pecho: 1 minuto 2 segundos 75 centésimas.
Mariposa: 59 segundos 80 centésimas.
Libre: 48 segundos 15 centésimas.
Usted debe averiguar el tiempo total de la carrera del equipo ganador y representarlo en minutos, segundos y centésimas.


Para recordar:

1 minutos son 60 segundos.
1 segundo son 100 centesimas."""

"""Espalda= "00:52:15"
Pecho = "01:02:75"
Mariposa= "00:59:80"
Libre= "00:48:15"


minutos= int(Espalda[0:2]) + int(Pecho[0:2]) + int(Mariposa[0:2]) + int(Libre[0:2])
segundos= int(Espalda[3:5])+ int(Pecho[3:5]) + int(Mariposa[3:5]) + int(Libre[3:5])
milisegundos = int(Espalda[6:8]) + int(Pecho[6:8]) + int(Mariposa[6:8]) + int(Libre[6:8])
#minutos= int(Espalda[0:3])*60 + int(Pecho[0:3])*60 + int(Mariposa[0:3])*60 + int(Libre[0:3])*60

milseg= divmod(milisegundos, 100)
segundostotales= segundos + minutos*60 + milseg[0]
mintot= divmod(segundostotales, 60)
minutostotales= mintot[0]
milisegundostotales= segundostotales *100 + milseg[1]
Tiempo = str(mintot[0])+":"+ str(mintot[1])+":"+str(milseg[1])
print(minutos,segundos,milisegundos, "minutos totales",minutostotales,"segundos totales",segundostotales,
"milisegundos totales",milisegundostotales,
      "\n",Tiempo)"""

"""Espalda= "00:52:15"
Pecho = "01:02:75"
Mariposa= "00:59:80"
Libre= "00:48:15" """

Espalda= 52*100 + 15
Pecho = 62*100 +75
Mariposa= 59*100 +80
Libre= 48*100 + 15

total = Espalda+Pecho+Mariposa+Libre

minuto = total//6000
resto = total%6000
segundos = resto//100
milisegundos = resto%100

print(minuto,segundos,milisegundos)
