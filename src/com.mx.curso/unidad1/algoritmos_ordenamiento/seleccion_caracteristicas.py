# Algoritmo de ordenamiento: Selección
caracteristicas = [
    ("Edad: ", 0.56),
    ("Educación: ", 0.88), 
    ("Ingresos: ", 0.72),
    ("Ciudad: ", 0.30),
    ("Género: ", 0.33),
    ("Ocupación: ", 0.68),
    ("Experiencia: ", 0.91),
    ("Horas_trabajo: ", 0.60)
]

print("Puntuaciones desordenadas: ", caracteristicas)

longitud = len(caracteristicas)
for i in range(longitud-1):
    max_index = i
    for j in range(i+1, longitud):
        if caracteristicas[j][1] > caracteristicas[max_index][1]:
            max_index = j
    caracteristicas[i], caracteristicas[max_index] = caracteristicas[max_index], caracteristicas[i]

print("\nCaracterísticas: ", caracteristicas)