capitulos=("CODIGO NO RECONOCIDO",
           "Cap.1: Ciertas enfermedades infecciosas y parasitarias ",
           "Cap.2: Tumores [neoplasias]",
           "Cap.3: Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad",
           "Cap.4: Enfermedades endocrinas, nutricionales y metabólicas",
           "Cap.5: Trastornos mentales y del comportamiento",
           "Cap.6: Enfermedades del sistema nervioso ",
           "Cap.7: Enfermedades del ojo y sus anexos",
           "Cap.8: Enfermedades del oído y de la apófisis mastoides",
           "Cap.9: Enfermedades del sistema circulatorio",
           "Cap.10: Enfermedades del sistema respiratorio",
           "Cap.11: Enfermedades del sistema digestivo",
           "Cap.12: Enfermedades de la piel y del tejido subcutáneo",
           "Cap.13: Enfermedades del sistema osteomuscular y del tejido conjuntivo",
           "Cap.14:Enfermedades del sistema genitourinario",
           "Cap.15: Embarazo, parto y puerperio",
           "Cap.16: Ciertas afecciones originadas en el período perinatal",
           "Cap.17: Malformaciones congénitas, deformidades y anomalías cromosómicas",
           "Cap.18: Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte",
           "Cap.19: Traumatismos, envenenamientos y algunas otras consecuencias de causas externas",
           "Cap.20: Causas externas de morbilidad y de mortalidad",
           "Cap.21: Factores que influyen en el estado de salud y contacto con los servicios de salud",
           "Cap.22: Códigos para propósitos especiales",)
# Carga de datos y sin mensajes
nombrePaciente = input()
codigo = input()
monto_base = int(input())

# Monto fijo inicial
montoFijoInicial = 25000

#  La variable letra que obtiene el primer elemento del codigo
letra = codigo[0]


# El bloque obtiene los dos digitos del bloque ( solo posiciones 1 y 2, el 3 no se incluye)
bloque = int(codigo[1:3])


# num_derecha pbtene los digitos a la derecha del punto (desde la posicion 4 hasta el final)
num_derecha = int(codigo[4:])

# Determnando el capitulo
if letra=="A" or letra=="B": # A00 a B99
    capitulo_desc = capitulos[1]
elif letra == "C": # C00 a C97
    capitulo_desc = capitulos[2]
elif letra == "D":
    if 0 <= bloque <= 48: # D00 a D48
        capitulo_desc = capitulos[2]
    elif 50 <= bloque <= 89: # D50 a D89
        capitulo_desc = capitulos[3]
elif letra == "E": # E00 a E90
    capitulo_desc = capitulos[4]
elif letra == "F": #  F00 a F99
    capitulo_desc = capitulos[5]
elif letra == "G": #  G00 a G99
    capitulo_desc = capitulos[6]
elif letra == "H":
    if 0 <= bloque <= 59: # H00 a H59
        capitulo_desc = capitulos[7]
    elif 60 <= bloque <= 95: #  H60 a H95
        capitulo_desc = capitulos[8]
elif letra == "I": # I00 a I99
    capitulo_desc = capitulos[9]
elif letra == "J": # J00 a J99
    capitulo_desc = capitulos[10]
elif letra == "K": # K00 a K93
    capitulo_desc = capitulos[11]
elif letra == "L": # L00 a L99
    capitulo_desc = capitulos[12]
elif letra == "M": #  M00 a M99
    capitulo_desc = capitulos[13]
elif letra == "N": # N00 a N99
    capitulo_desc = capitulos[14]
elif letra == "O": # O00 a O99
    capitulo_desc = capitulos[15]
elif letra == "P": # P00 a P96
    capitulo_desc = capitulos[16]
elif letra == "Q": # Q00 a Q99
    capitulo_desc = capitulos[17]
elif letra == "R": #  R00 a R99
        capitulo_desc = capitulos[18]
elif letra == "T" or letra == "S": # S00 a T98
    capitulo_desc = capitulos[19]
elif letra == "V" or letra == "W" or letra == "X" or letra == "Y": # V01 a Y98
    capitulo_desc = capitulos[20]
elif letra == "Z": # Z00 a Z99
    capitulo_desc = capitulos[21]
elif letra == "U": # U00 a U99
    capitulo_desc = capitulos[22]

# Calculo del monto
monto_final = monto_base + montoFijoInicial

if "A" <= letra <= "L":
    monto_final += 25000
elif "M" <= letra <= "Z" and letra != "U":
    monto_final += 40000
elif letra == "U":
    monto_final += 100000

# Agregar el porcentaje del numero a la derecha
porcentaje = (num_derecha * monto_final) / 100
monto_final += porcentaje

# Sañidas por consola segun el enunciado
print("Beneficiario:", nombrePaciente)
print("Codigo:", codigo)
print("Capitulo:", capitulo_desc)
print("Monto a pagar:", monto_final)
