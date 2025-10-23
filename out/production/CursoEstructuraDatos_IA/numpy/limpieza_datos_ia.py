import numpy as np

# Creamos el conjunto de datos:
np.random.seed(200)
datos = np.random.rand(10, 3) * 100

fila = np.random.randint(0, 3)
columna = np.random.randint(0, 3)

valor_erroneo = 2.7182818284
cantidad_nan = 5

# Introduce una fila de datos erróneos y valores faltantes:
for i in range(len(datos)):
    for j in range(len(datos[i])):
        datos[3][j] = valor_erroneo

# Posición aleatorias para almacenar nan:
# Shape[0] = fila y Shape[1] = columna.
posiciones = [(i, j) for i in range(datos.shape[0]) for j in range(datos.shape[1])]
posiciones_nan = np.random.choice(len(posiciones), size = cantidad_nan, replace=False)

# Asignamos el nan en esas posicines:
for i in posiciones_nan:
    fila, columna = posiciones[i]
    datos[fila, columna] = np.nan

print("Datos originales: ")
print(datos)

# Eliminar datos erróneos:
datos_limpios = np.delete(datos, 3, 0)
print("\nDatos limpios: ")
print(datos_limpios)

