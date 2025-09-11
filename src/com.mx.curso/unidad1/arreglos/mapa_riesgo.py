# Mapa de riesgo

# Crea una matriz de 8x8:

matriz = [[0,1,2,1,2,0,1,1],
          [0,1,2,1,2,0,1,1],
          [0,1,2,1,2,0,1,1],
          [0,1,2,1,2,0,1,1],
          [0,1,2,1,2,0,1,1],
          [0,1,2,1,2,0,1,1],
          [0,1,2,1,2,0,1,1],
          [0,1,2,1,2,0,1,1]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()

area_riesgo = 0 # 2 
area_precuacion = 0 # 1

# Contabilizar las áreas: 
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 2:
            area_riesgo += 1
        elif matriz[i][j] == 1:
            area_precuacion += 1
    print()

print(f"Área de riesgo (2): {area_riesgo}")
print(f"Área de precaución (1): {area_precuacion}")

# Actualizar la matriz de navegación:
# Cambiar todos los dos por unos:
print("---Actualización de matriz de navegación---")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 2:
            matriz[i][j] == 1

area_riesgo_actualizada = 0
area_precuacion_actualizada = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
        if matriz[i][j] == 2:
            area_riesgo_actualizada += 1
        if matriz[i][j] == 1:
            area_precuacion_actualizada += 1
    print()

print(f"Área de riesgo actualizada: {area_riesgo_actualizada}")
print(f"Área de precaución actualizada: {area_precuacion_actualizada}")
