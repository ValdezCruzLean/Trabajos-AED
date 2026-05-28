"""
7. Votación en el Congreso
En el Congreso se vota la sanción de una ley muy importante.
Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra,
 e informe el porcentaje obtenido en cada caso."""

votosfavor= int(input("Ingrese el total de votos a favor : "))
votoscontra= int(input("Ingrese el total de votos en contra : "))

votos = votosfavor + votoscontra

porcentajefavor= (votosfavor*100)/votos
porcentajecontra= (votoscontra*100)/votos

print("El",f"{porcentajefavor:.2f}"," % del congreso esta a favor de la sansion de la ley",
"\nEl",f"{porcentajecontra:.2f}","% del congreso esta encontra de la sansion de la ley")