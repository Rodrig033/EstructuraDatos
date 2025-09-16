# Matriz de conexiones para una red neuronal simple:
import numpy as np
import time 

entrada = [1, 2, 3]

pesos = [[1, 3],
         [1, 4],
         [7, 8]]

vector = []
star_time = time.time()
sumar = []
suma = 0
suma_dos = 0

for i in range(len(pesos)):
    # Primer columna:
    first = pesos[i][0] * entrada[i]
    vector.append(first)

    
for i in range(len(pesos)):
     # Segunda columna:
     second = pesos[i][1] * entrada[i]
     vector.append(second)

# Columna:
for peso in range(len(pesos[0])):
     suma = 0
     # Fila: 
     for element in range(len(entrada)):
          suma += entrada[element] * pesos[element][peso]
     sumar.append(suma)
    

end_time = time.time()

print("\nInicio: ", star_time)
print(vector)
print("Vector final: ",sumar)
print("Final: ", end_time - star_time)