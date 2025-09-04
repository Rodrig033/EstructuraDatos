import time

def tiene_duplicados_lineal(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# Pruebas con diferentes tamaños:
sizes = [100, 1000, 1000000]

for n in sizes:
    arr = list(range(n))

    star_time = time.time()
    tiene_duplicados_lineal(arr)
    end_time = time.time()

    print(f"Búsqueda de duplicados en un arreglo de {n} elementos: {end_time - star_time: .6f} segundos.")