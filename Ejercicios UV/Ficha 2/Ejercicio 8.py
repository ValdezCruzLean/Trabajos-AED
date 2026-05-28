"""
8. Rinde de un Campo Agricola
Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela.
Se pide ingresar el largo y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m**2 se obtienen 2 quintales."""

largo = int(input("Ingrese el largo de la parcela en metros : "))
ancho= int(input("Ingrese el ancho de la parcela en metros : "))

area = largo * ancho

rinde = area / 10

quintales = rinde * 2

print("La parcela puede producir",f"{quintales:.2f}"," quintales de trigo en",rinde,"metros cuadrados")