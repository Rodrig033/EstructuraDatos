# Matriz recomedación películas: 
import pandas as pd 
matriz = [

    [5,	5,	4,	5,	5,	1,	5,	5,	3,	5,	3,	4,	4],
    [2,	5,	4,	5,	5,	3,	5,	4,	5,	5,	3,	5,	3],
    [2,	5,	5,	5,	4,	3,	5,	4,	4,	5,	2,	4,	3],
    [4,	5,	4,	5,	5,	4,	4,	5,	5,	5,	3,	4,	2],
    [5,	4,	4,	5,	5,	4,	5,	5,	3,	5,	1,	5,	1],
    [3,	5,	3,	5,	3,	5,	2,	1,	3,	5,	3,	1,	1],
    [2,	4,	5,	3,	5,	2,	5,	3,	3,	4,	1,	3,	2],
    [4,	5,	5,	2,	5,	1,	3,	5,	5,	4,	3,	1,	3],
    [3,	2,	5,	2,	5,	2,	3,	2,	5,	4,	5,	4,	2],
    [3,	5,	2,	5,	3,	1,	1,	5,	1,	5,	3,	1,	5],
    [5,	1,	5,	5,	5,	4,	4,	1,	4,	5,	4,	1,	5],
    [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5],
    [5,	4,	3,	5,	5,	1,	4,	2,	3,	5,	2,	1,	5]
]

columnas = matriz[0]

# Imprimir la matriz de calificaciones
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end= "") 
    print()

# Calcular la calificación promedio de una pelicula:
suma = 0
pelicula = 9

for i in range(len(matriz)):
    suma += int(matriz[i][pelicula])

print(f"\nLa suma de calificaciones pelicula uno: {suma}")
promedio = suma / len(matriz)
print(f"El promedio de calificaciones pelicula uno: {promedio} ")
calificaciones_usuario = matriz[0]
print(f"Calificaciones MARTIN: {calificaciones_usuario}")


# Arreglo que muestre la calificación más alta y más baja

df = pd.DataFrame(matriz, columns=columnas)
print("\n")
print(df.to_string(index=False))



