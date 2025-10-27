# Búsqueda Binaria:
import random

clientes = [random.randint(1, 1000) for _ in range(500)]

# QuickSort:
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

quicksort(clientes)
print(clientes)

def busqueda_binaria(lista, objetivo):
    low, high = 0, len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            low = mid + 1
        else:
            high = mid - 1
    return -1

cliente_especifico = int(input("Ingrese el ID del cliente: "))
posicion = busqueda_binaria(clientes, cliente_especifico)

if posicion != -1:
    print(f"Cliente encontrado en la posición {posicion}.")
else:
    print("Cliente no encontrado.")