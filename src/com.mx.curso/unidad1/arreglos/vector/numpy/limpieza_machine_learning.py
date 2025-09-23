import numpy as np

# Crear matriz:
np.random.seed(50)
data = np.random.rand(6, 4) * 100

print("Datos originales:")
print(data)

indices_eliminar = [0, 4]
limpiar_data = np.delete(data, indices_eliminar, axis=0)
print("\nDatos limpios: ")
print(limpiar_data)