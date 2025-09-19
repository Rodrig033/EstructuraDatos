# Entrenamiento de una red neuronal:
import numpy as np
import time
entrada = [1, 2, 5]

# Matriz pesos 3 x 2:
pesos = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

salida = [0,0,0,0]
start_time = time.time()

for j in range(len(pesos[0])):
    for i in range(len(pesos)):
        salida[j] += entrada[i] * pesos[i][j]

end_time = time.time()

print("Inicio: ", start_time)
print("Vector Entrada: ", entrada)
print("Matriz pesos: ", pesos)
print("Salida: ", salida)
print("Final: ", end_time - start_time)