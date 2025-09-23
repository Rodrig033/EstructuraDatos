# Operaciones de limpieza de datos:
import numpy as np

datos = np.array([[10, 10, 10], 
                 [20, 20, 20],
                 [30, 30, 30]])

print("Datos originales: \n", datos)

datos_limpios = np.delete(datos, 1, axis = 0) # Elimina la segunda fila
print("Datos después de eliminar la segunda fila: \n", datos_limpios)

# Introducir datos erroneos:
datos[0] = [10,-2,10]
datos[1] = [20,-2,20]
datos[2] = [30,30,30]
print("Datos con errores introducidos:\n", datos)



valores_negativos = []
for i in range(len(datos)):
    for j in range(len(datos[i])):
        if datos[i][j] < 0:
            valores_negativos.append((i, j))

datos_limpios = np.delete(datos, valores_negativos, axis=0) # Eliminar datos negativos
print("Datos limpios después de eliminar valores negativos", datos_limpios)