import time, random

# Bubble Sort vs Insertion Sort

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        actual = a[i]
        j = i - 1
        while j >= 0 and a[j] > actual:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = actual
    return a


tamaños = [100, 1000, 10000]

print(f"{'Tamaño':<10}{'Tiempo Burbuja (s)':<22}{'Tiempo Inserción (s)'}")
print("-" * 52)

for n in tamaños:
    datos = [round(random.uniform(0, 1), 2) for _ in range(n)]

    # Tiempo de Burbuja
    inicio_bubble = time.time()
    bubble_sort(datos)
    tiempo_bubble = time.time() - inicio_bubble

    # Tiempo de Inserción
    inicio_insertion = time.time()
    insertion_sort(datos)
    tiempo_insertion = time.time() - inicio_insertion

    # Ingreso losa datos obtenidos en la tabla: 
    print(f"{n:<10}{tiempo_bubble:<22.6f}{tiempo_insertion:.6f}")