# Aves migratorias:
migratory_birds = [1, 1, 2, 2, 3]
tipos = []
repetidos = []
tipo_pequeño = 0

# Almacenar solo los tipos:
for i in range(len(migratory_birds)):
    for j in range(len(migratory_birds)):
        if i != j:
            if migratory_birds[i] != migratory_birds[j] and migratory_birds[i] not in tipos:
                tipos.append(migratory_birds[i])

# Repetidos
for i in range(len(migratory_birds)):
    for j in range(len(migratory_birds)):
        if i != j:
            if migratory_birds[i] == migratory_birds[j] and migratory_birds[i] not in repetidos:
                repetidos.append(migratory_birds[i])

# Recorrer el arreglo y comparar para conseguir el valor pequeño:
for i in range(len(tipos)):
    for j in range(len(tipos)):
        if i != j:
            if migratory_birds[i] < migratory_birds[j]:
                tipo_pequeño = migratory_birds[i]


# Valores: 
print("Tipos de aves: ", tipos)
print("Repetidos: ",repetidos)
print("Tipo pequeño: ", tipo_pequeño)