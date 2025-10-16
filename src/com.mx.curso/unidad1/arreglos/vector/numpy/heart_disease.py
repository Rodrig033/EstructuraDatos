import numpy as np

# Dataset cleveland
data = np.genfromtxt('src/com.mx.curso/unidad1/arreglos/vector/numpy/processed.cleveland.data', delimiter= ',', dtype='object')

# Cargar solo las primeras 4 columnas:
datos_numericos = np.genfromtxt('src/com.mx.curso/unidad1/arreglos/vector/numpy/processed.cleveland.data', delimiter=',', usecols=(1,2,3,4))
print(datos_numericos)

# Elimina indices:
indices_eliminar = [0, 2, 3]
# Elimina las filas con los índices:
datos_limpios = np.delete(datos_numericos, indices_eliminar, axis=0)
print("\n----- Datos limpios -----")
print(datos_limpios)

datos_limpios[0, 1] = np.nan
datos_limpios[1, 1] = np.nan
datos_limpios[0, 2] = np.nan
datos_limpios[2, 3] = np.nan


print("\n--- Datos faltantes ---")
print(datos_limpios)

media_columna = np.nanmean(datos_limpios, axis=0)
print("\n--- Media de cada columna ---")
print("\n--- Mediana del dataframe ---")
print(media_columna)
print("Mediana: ", np.nanmedian(datos_limpios))

# Remplazar los índices con Nan:
for i in range(datos_limpios.shape[0]):
    for j in range(datos_limpios.shape[1]):
        if np.isnan(datos_limpios[i, j]):
            datos_limpios[i, j] = media_columna[j]

print("\n--- Data Frame limpio ---")
print(datos_limpios)