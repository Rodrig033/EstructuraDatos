import numpy as np

# Dataset cleveland:
data = np.genfromtxt('src/com.mx.curso/unidad1/arreglos/vector/numpy/processed.cleveland.data', delimiter= ',', dtype='object')

# Cargar solo las primeras 4 columnas:
datos_numericos = np.genfromtxt('src/com.mx.curso/unidad1/arreglos/vector/numpy/processed.cleveland.data', delimiter=',', usecols=(1,2,3,4))
print(datos_numericos)

# Elimina indices:
indices_eliminar = [0, 2, 3]
# Elimina las filas con los índices:
datos_limpios = np.delete(datos_numericos, indices_eliminar, axis=0)
print("\n--- Datos limpios ---")
print(datos_limpios)

datos_limpios[0, 1] = np.nan
datos_limpios[1, 1] = np.nan
datos_limpios[0, 2] = np.nan
datos_limpios[2, 3] = np.nan


print("\n--- Datos faltantes ---")
print(datos_limpios)

media_columna = np.nanmean(datos_limpios, axis=0)
print("\n--- Media de cada columna ---")
print(media_columna)
print("Mediana: ", np.nanmedian(datos_limpios))
print("Desviación estándar: ", np.std(datos_limpios))

# Remplazar los índices con Nan:
for i in range(datos_limpios.shape[0]):
    for j in range(datos_limpios.shape[1]):
        if np.isnan(datos_limpios[i, j]):
            datos_limpios[i, j] = media_columna[j]

print("\n--- Data Frame limpio ---")
print(datos_limpios)
print("\nMedia: ", np.mean(datos_limpios))
print("Mediana: ", np.nanmedian(datos_limpios))
print("Desviación estándar: ", np.std(datos_limpios))

# Análisis especifíco:
glucosa = []
for i in range(len(data)):
    glucosa.append(float(data[i][4].decode()))

promedio_glucosa = np.mean(glucosa)
print("Promedio de la glucosa: ", round(promedio_glucosa, 1))

# Calcular la maxima frecuencia cardíaca: 
frecuencia_cardiaca = []
for i in range(len(data)):
    frecuencia_cardiaca.append(float(data[i][7].decode()))

maxima_frecuencia = max(frecuencia_cardiaca)
print("Maxima frecuencia cardíaca: ",maxima_frecuencia)

# Calcular la edad con la frecuencia cardíaca más alta:
edad = 0
for fila in range(len(data)):
    for columna in range(len(data)):
        if fila == maxima_frecuencia:
            edad,

print(edad)