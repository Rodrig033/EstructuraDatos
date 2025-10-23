# Creación de una matriz 3x3:

matriz = [
    [0, 1, 1],
    [2, 3, 4], 
    [5, 6, 7]
]

# Imprimir elementos (Fila x Columna):


print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])

print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])

print(matriz[2][0])
print(matriz[2][1])
print(matriz[2][2])

# Modificar el valor de un elemento de la matriz:
matriz[2][0] = 100

print(matriz[2][0])


print("\nMatriz 4x4: ")

matriz_4 = [
    [0, 1, 1, 1],
    [2, 3, 4, 5], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(matriz_4[0][0])
print(matriz_4[0][1])
print(matriz_4[0][2])
print(matriz_4[0][3])

print(matriz_4[1][0])
print(matriz_4[1][1])
print(matriz_4[1][2])
print(matriz_4[1][3])

print(matriz_4[2][0])
print(matriz_4[2][1])
print(matriz_4[2][2])
print(matriz_4[2][3])

print(matriz_4[3][0])
print(matriz_4[3][1])
print(matriz_4[3][2])
print(matriz_4[3][3])


# Modificar valor matriz 4x4:
matriz_4[3][3] = 33
print(matriz_4[3][3])