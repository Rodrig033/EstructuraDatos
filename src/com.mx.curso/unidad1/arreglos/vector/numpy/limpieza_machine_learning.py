import numpy as np

# Crear matriz:
np.random.seed(50)
data = np.random.rand(6, 4) * 100
# Se usa punto flotante porque nos devuelve datos más especificos 

print("Datos originales:")
print(data)

# Axis = 0 se refiere a la fila y Axis = 1 se refiere a la columna
limpiar_data = np.delete(data, 0, axis = 0)
print("\nDatos limpios: ")
print(limpiar_data)