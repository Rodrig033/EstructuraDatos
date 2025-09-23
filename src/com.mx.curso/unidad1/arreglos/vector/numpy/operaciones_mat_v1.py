# Operaciones con matrices utilizando Numpy:
import numpy as np

# Crear una matriz: 
matriz_A = [[1,2,3], 
            [4,6,7], 
            [9,9,9]]

matriz_B = [[1,4,3], 
            [1,6,7], 
            [9,4,99]]

# Suma de matrices:
suma = np.add(matriz_A, matriz_B)
print("Suma de matrices: \n", suma)

# Multiplicación de matrices:
multipicacion = np.dot(matriz_A, matriz_B)
print("Multplicación de matrices: \n", suma)

# Producto punto:
Vector_E = np.array([1,2,3])
resultado = np.dot(matriz_A, Vector_E)
print("Producto punto: \n", resultado)