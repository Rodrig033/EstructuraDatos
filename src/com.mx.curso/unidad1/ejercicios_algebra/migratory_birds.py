# Aves migratorias:
migratory_birds = [1, 1, 2, 2, 3]
tipo_pequeño = 0
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
minima_nota = 0
for i in enumerate(migratory_birds):
    nota_min = min(migratory_birds)
    if nota_min < minima_nota:
        minima_nota = nota_min
        type_min = migratory_birds

print(minima_nota)