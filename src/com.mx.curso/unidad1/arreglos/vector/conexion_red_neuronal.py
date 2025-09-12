# Matriz de conexiones para una red neuronal simple:
import numpy as np
import time 

entrada = [1, 2, 3]

pesos = [[1, 3],
         [1, 4],
         [7, 8]]

vector = []
star_time = time.time()
sumar = 0


for i in range(len(pesos)):
    # Primer columna:
    sumar += pesos[i][0] * entrada[i]
    vector.append(sumar)
    # Segunda columna:


end_time = time.time()

print("\nInicio: ", star_time)
print(vector)
print(sumar)
print("Final: ", end_time - star_time)