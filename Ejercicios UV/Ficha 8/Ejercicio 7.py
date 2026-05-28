import random

# Configuramos la semilla para que los resultados sean siempre los mismos
random.seed(76)

# Variables para los contadores y acumuladores
cant_pares_mult_6 = 0
cant_mayores_primero = 0
cant_segundo_millar = 0

total_numeros = 5000
primer_numero = None

# Generamos y procesamos la serie de números
for i in range(total_numeros):
    # Generamos el número aleatorio entre 1 y 65000 (inclusive)
    num = random.randint(1, 65000)

    # Guardamos el primer número de la serie para las comparaciones posteriores
    if i == 0:
        primer_numero = num
    else:
        # Punto 2: Números mayores al primero de la serie (sin incluirlo)
        if num > primer_numero:
            cant_mayores_primero += 1

    # Punto 1: Números pares que sean múltiplos de 6
    # (Nota: Todo número múltiplo de 6 ya es par por definición, pero lo evaluamos explícitamente)
    if num % 2 == 0 and num % 6 == 0:
        cant_pares_mult_6 += 1

    # Punto 3: Números que pertenecen al segundo millar (entre 1001 y 2000 inclusive)
    if 1001 <= num <= 2000:
        cant_segundo_millar += 1

# Punto 4: Cálculo del porcentaje del punto 2 respecto al total (5000)
porcentaje_mayores = (cant_mayores_primero / total_numeros) * 100

# Mostramos los resultados en la consola de forma limpia
print("--- RESULTADOS DEL ANÁLISIS ---")
print(f"Cantidad de números pares que son múltiplos de 6: {cant_pares_mult_6}")
print(f"Cantidad de números que son mayores al primero ({primer_numero}): {cant_mayores_primero}")
print(f"Cantidad de números que pertenecen al segundo millar (1001-2000): {cant_segundo_millar}")
print(f"Porcentaje que representan los mayores al primero respecto al total: {porcentaje_mayores:.2f}%")