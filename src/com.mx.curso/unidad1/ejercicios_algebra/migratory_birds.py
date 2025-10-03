# Aves migratorias:
migratory_birds = [1, 1, 2, 2, 3]
type_1 = 0
type_2 = 0 
type_3 = 0

# Almacenar todos los tipos:
for i in range(len(migratory_birds)):
    if migratory_birds[i] == 1:
        type_1 += 1
    elif migratory_birds[i] == 2:
        type_2 += 1
    elif migratory_birds[i] == 3:
        type_3 += 1

# Recorrer el arreglo y comparar para conseguir el valor pequeño:
for i in range(len(migratory_birds)):
    if i < 